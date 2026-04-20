from graph.workflow import build_graph
from config import Config
from tools.logger import setup_logger, log_info, log_error


def run_pipeline(file_path: str):
    """
    Runs the full multi-agent fraud intelligence pipeline
    """

    # Initialize logger once
    setup_logger()

    try:
        log_info(" Pipeline started")
        log_info(f" Processing file: {file_path}")

        # Build graph
        app = build_graph()

        # Initial state
        state = {
            "file_path": file_path,
            "data": None,
            "processed_data": None,
            "analysis": None,
            "final_output": None,
            "report_json": None,
            "status": "start",
            "message": None,
            "retry_count": 0
        }

        # Run workflow
        result = app.invoke(state)

        log_info(" Pipeline executed successfully")

        return result

    except Exception as e:
        log_error(f" Pipeline failed: {str(e)}")
        return None


def print_output(result: dict):
    """
    Pretty prints the final report (CLI mode)
    """

    print("\n" + "=" * 60)
    print("📊 FINAL FRAUD INTELLIGENCE REPORT")
    print("=" * 60)

    if not result:
        print(" No result returned")
        return

    output = result.get("final_output")

    if output:
        print(output)
    else:
        print(" No report generated")

    print("\n" + "=" * 60)


def main():
    """
    Entry point of the system
    """

    try:
        print("\n Starting Financial Risk Intelligence System...\n")

        file_path = Config.DATA_PATH

        result = run_pipeline(file_path)

        print_output(result)

        print("\n System completed successfully\n")

    except Exception as e:
        print(f"\n System Error: {str(e)}\n")


if __name__ == "__main__":
    main()