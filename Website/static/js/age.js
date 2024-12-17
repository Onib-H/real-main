document.addEventListener("DOMContentLoaded", () => {
    const birthdayInput = document.getElementById("birthday");
    const ageInput = document.getElementById("age");

    birthdayInput.addEventListener("input", () => {
        const birthdayValue = birthdayInput.value;
        if (birthdayValue) {
            const age = calculateAge(new Date(birthdayValue));
            ageInput.value = age >= 0 ? age : "";
        } else {
            ageInput.value = ""; // Clear age if no birthday is set
        }
    });

    function calculateAge(birthday) {
        const today = new Date();
        let age = today.getFullYear() - birthday.getFullYear();
        const isBirthdayPassedThisYear =
            today.getMonth() > birthday.getMonth() ||
            (today.getMonth() === birthday.getMonth() && today.getDate() >= birthday.getDate());
        if (!isBirthdayPassedThisYear) {
            age -= 1;
        }
        return age;
    }
});
