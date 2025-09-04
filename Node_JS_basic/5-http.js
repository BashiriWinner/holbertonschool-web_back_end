async function countStudents(path) {
  if (!path) {
    throw new Error('Cannot load the database');
  }
  try {
    const data = await fs.readFile(path, 'utf8');
    const lines = data.trim().split('\n').filter(line => line.trim() !== '');
    if (lines.length <= 1) {
      throw new Error('Cannot load the database');
    }
    const students = lines.slice(1);
    const totalStudents = students.length;
    
    const fields = {};
    students.forEach((line) => {
      const student = line.split(',');
      if (student.length < 4) return;
      const field = student[3].trim(); 
      const name = student[0].trim(); 
      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(name);
    });
    
    let output = `Number of students: ${totalStudents}\n`;
    for (const [field, list] of Object.entries(fields)) {
      output += `Number of students in ${field}: ${list.length}. List: ${list.join(', ')}\n`;
    }
    return output.trim();
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}
