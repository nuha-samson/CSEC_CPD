import React from 'react';
import 'styles.css'
import { useForm } from "react-hook-form";

function App() {
  const {register,handleSubmit,reset,formState: { errors },} = useForm();
  function onSubmit(data) {
    alert("Form Submitted!");
    reset();
  }
  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <h2>Contact Us</h2>
      <div>
        <label>Name</label>
        <input type="text" placeholder="Enter your name"
        {...register("name", {required: "Name is required",})}/>
        {errors.name && <p>{errors.name.message}</p>}
      </div>

      <div>
        <label>Email</label>

        <input type="email" placeholder="Enter your email"
          {...register("email", { required: "Email is required", pattern: {
          value: /^\S+@\S+\.\S+$/, message: "Invalid email",},
          })}/>

        {errors.email && <p>{errors.email.message}</p>}
      </div>
      <div>


        <label>Message</label>
        <textarea rows="5" placeholder="Write your message..."
          {...register("message", {required: "Message is required",minLength: {
          value: 10, message: "Message must be at least 10 characters",},
          })}/>


        {errors.message && <p>{errors.message.message}</p>}
      </div>
      <button type="submit">Send Message</button>
    </form>
  );
}

export default App;
