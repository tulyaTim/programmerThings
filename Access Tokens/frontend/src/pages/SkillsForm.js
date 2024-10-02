import React, { useContext, useState } from 'react';
import axios from 'axios';
import AuthContext from '../context/AuthContext';

const SkillsForm = () => {
    const { AddSkills } = useContext(AuthContext);

  return (
    <form onSubmit={AddSkills}>
      <input
        type="text"
        name='name'
        placeholder="Skill Name"
        required
      />
      <select
        name='proficiency_level'
      >
        <option value={1}>Beginner</option>
        <option value={2}>Intermediate</option>
        <option value={3}>Advanced</option>
      </select>
      <button type="submit">Add Skill</button>
    </form>
  );
};

export default SkillsForm;
