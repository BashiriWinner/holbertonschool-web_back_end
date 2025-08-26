export default function getStudentIdsSum(students) { 
	return students.reduce((acc, students) => acc + student.id, 0); 
}
