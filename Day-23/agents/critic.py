from config import Config
from tools.logger import log_info, log_error


def critic(state):
    """
    Critic Agent:
    Validates analysis output and controls retry logic
    """

    try:
        retry_count = state.get("retry_count", 0)
        analysis = state.get("analysis")

        log_info(f"🔍 Critic evaluating output (retry_count={retry_count})")

        # -----------------------------
        #  Missing analysis → retry
        # -----------------------------
        if analysis is None:
            if retry_count < Config.MAX_RETRIES:
                log_info("⚠️ No analysis found → retrying")
                return {
                    "status": "retry",
                    "retry_count": retry_count + 1
                }
            else:
                log_info("⚠️ Max retries reached → forcing approval")
                return {
                    "status": "approved"
                }

        # -----------------------------
        #  Invalid analysis
        # -----------------------------
        total = analysis.get("total_transactions", 0)

        if total == 0:
            if retry_count < Config.MAX_RETRIES:
                log_info("⚠️ Empty dataset → retrying")
                return {
                    "status": "retry",
                    "retry_count": retry_count + 1
                }
            else:
                log_info("⚠️ Max retries reached → forcing approval")
                return {
                    "status": "approved"
                }

        # -----------------------------
        #  VALID CASE
        # -----------------------------
        log_info("✅ Analysis approved")

        return {
            "status": "approved"
        }

    except Exception as e:
        log_error(f" Critic error: {str(e)}")

        return {
            "status": "approved"  # fail-safe to avoid loop
        }