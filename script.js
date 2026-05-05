function calculate() {
    let s1 = Number(document.getElementById("sub1").value);
    let s2 = Number(document.getElementById("sub2").value);
    let s3 = Number(document.getElementById("sub3").value);
    let s4 = Number(document.getElementById("sub4").value);
    let s5 = Number(document.getElementById("sub5").value);

    let total = s1 + s2 + s3 + s4 + s5;
    let avg = total / 5;

    let grade = "";

    if (avg >= 90) grade = "A+";
    else if (avg >= 80) grade = "A";
    else if (avg >= 70) grade = "B";
    else if (avg >= 60) grade = "C";
    else if (avg >= 50) grade = "D";
    else grade = "F";

    document.getElementById("total").innerText = "Total Marks: " + total;
    document.getElementById("average").innerText = "Average: " + avg.toFixed(2) + "%";
    document.getElementById("grade").innerText = "Grade: " + grade;
}