def calculate_gcs():
    # Gather input from user
    eye_response = int(input("Enter the Eye Response score (1-4): "))
    verbal_response = int(input("Enter the Verbal Response score (1-5): "))
    motor_response = int(input("Enter the Motor Response score (1-6): "))

    # Validate input scores
    if not (1 <= eye_response <= 4) or not (1 <= verbal_response <= 5) or not (1 <= motor_response <= 6):
        print("Invalid input scores. Scores should be in the range 1-4 for Eye Response, 1-5 for Verbal Response, and 1-6 for Motor Response.")
        return None

    # Calculate GCS score
    gcs_score = eye_response + verbal_response + motor_response

    # Determine GCS category
    if 13 <= gcs_score <= 15:
        gcs_category = "Mild"
    elif 9 <= gcs_score <= 12:
        gcs_category = "Moderate"
    elif 3 <= gcs_score <= 8:
        gcs_category = "Severe"
    else:
        gcs_category = "Undefined"

    # Print results
    print("Glasgow Coma Scale (GCS) Calculation:")
    print(f"Eye Response: {eye_response}")
    print(f"Verbal Response: {verbal_response}")
    print(f"Motor Response: {motor_response}")
    print(f"GCS Score: {gcs_score}")
    print(f"GCS Category: {gcs_category}")


# Run the GCS calculation
calculate_gcs()
