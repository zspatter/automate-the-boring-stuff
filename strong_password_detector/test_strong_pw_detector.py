from strong_password_detector import strong_pw_detector

invalid_pws = ['12345678', 'password123', 'PASSWORD1a', 'Ab1!', 'PASSWORD1@']
valid_pws = ['Password1!', 'xY@5bapt', 'saMple@#1', 'Short12@']


def test_check_pw_strength():
    for pw in invalid_pws:
        assert not strong_pw_detector.check_pw_strength(pw)

    for pw in valid_pws:
        assert strong_pw_detector.check_pw_strength(pw)
