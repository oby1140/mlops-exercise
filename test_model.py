import os
import json
import app

# Test if model file is created
def test_model_file_created():
    app.main()  # Assuming the main function encapsulates the training logic
    assert os.path.exists('models/model.pkl')

# Test model performance and version comparison
def test_model_score():
    score = app.main()  # Assuming the main function returns the score
    assert isinstance(score, float)
    assert 0.0 <= score <= 1.0
    
    # Load the model scores
    with open('model_scores.json', 'r') as f:
        model_scores = json.load(f)
    
    # Get the latest model score
    latest_score = model_scores[-1]['score']
    
    # Compare the latest score with the current score
    # This test ensures our model doesn't get worse over time
    assert score >= latest_score, f"Current model score {score} is worse than the latest score {latest_score}"