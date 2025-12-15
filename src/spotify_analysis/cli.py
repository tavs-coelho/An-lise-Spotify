"""Command-line interface for Spotify Analysis."""

import argparse
import sys
from pathlib import Path


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Spotify Music Popularity Analysis CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 1.0.0"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Train command
    train_parser = subparsers.add_parser("train", help="Train models")
    train_parser.add_argument("--data", type=str, help="Path to training data")
    train_parser.add_argument("--model", type=str, default="xgboost", help="Model to train")
    
    # Predict command
    predict_parser = subparsers.add_parser("predict", help="Make predictions")
    predict_parser.add_argument("--model", type=str, required=True, help="Path to model")
    predict_parser.add_argument("--data", type=str, required=True, help="Path to data")
    predict_parser.add_argument("--output", type=str, help="Output file path")
    
    # API command
    api_parser = subparsers.add_parser("api", help="Start API server")
    api_parser.add_argument("--host", type=str, default="0.0.0.0", help="Host address")
    api_parser.add_argument("--port", type=int, default=8000, help="Port number")
    
    # Dashboard command
    dashboard_parser = subparsers.add_parser("dashboard", help="Start Streamlit dashboard")
    
    args = parser.parse_args()
    
    if args.command == "train":
        print(f"Training {args.model} model...")
        print("For detailed training, please use the Python API or Jupyter notebook.")
    
    elif args.command == "predict":
        print(f"Loading model from {args.model}...")
        print(f"Making predictions on {args.data}...")
        print("For detailed predictions, please use the Python API or REST API.")
    
    elif args.command == "api":
        print(f"Starting API server on {args.host}:{args.port}...")
        print("Run: uvicorn api:app --host {args.host} --port {args.port}")
    
    elif args.command == "dashboard":
        print("Starting Streamlit dashboard...")
        print("Run: streamlit run app.py")
    
    else:
        parser.print_help()
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
