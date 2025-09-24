// src/pages/Home.jsx
import { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Calendar } from "@/components/ui/calendar";
import { GraduationCap, School, BookOpen } from "lucide-react";

export default function Home() {
  const [date, setDate] = useState(new Date());

  return (
    <div className="bg-black text-white font-sans">
      {/* HEADER */}
      <header className="absolute top-0 left-0 w-full flex justify-between items-center px-10 py-6 z-10">
        <div className="flex items-center gap-2 text-xl font-bold">
          🎓 EduSync-360
        </div>
        <nav className="flex gap-6">
          <a href="/" className="hover:text-blue-400">Home</a>
          <a href="/about" className="hover:text-blue-400">About Us</a>
          <a href="/courses" className="hover:text-blue-400">Courses</a>
          <a href="/results" className="hover:text-blue-400">Our Results</a>
          <a href="/admission" className="hover:text-blue-400">Registration</a>
          <a href="/contact" className="hover:text-blue-400">Contact Us</a>
        </nav>
      </header>

      {/* HERO SECTION */}
      <section
        className="relative h-[80vh] flex flex-col justify-center items-center bg-cover bg-center"
        style={{
          backgroundImage:
            "url('https://images.unsplash.com/photo-1523050854058-8df90110c9f1?auto=format&fit=crop&w=1600&q=80')",
        }}
      >
        <div className="bg-black bg-opacity-70 absolute inset-0"></div>
        <div className="relative z-10 text-center max-w-2xl mx-auto">
          <h1 className="text-5xl font-bold">Welcome to EduSync-360</h1>
          <p className="mt-4 text-lg italic text-gray-200">
            One platform to manage Students, Teachers, and Admins seamlessly.
          </p>
          <Button className="mt-6 bg-blue-600 hover:bg-blue-700">
            Get Started
          </Button>
        </div>
      </section>

      {/* FEATURES SECTION */}
      <section className="py-20 bg-gray-900 text-white">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-6xl mx-auto px-6">
          <Card className="bg-black bg-opacity-70 text-white">
            <CardContent className="p-6 flex flex-col items-center">
              <GraduationCap className="w-10 h-10 mb-3 text-blue-400" />
              <h3 className="font-semibold text-lg">For Students</h3>
              <p className="text-sm text-gray-300 text-center">
                Track attendance, access study materials, apply for leave,
                and view test results in one place.
              </p>
            </CardContent>
          </Card>
          <Card className="bg-black bg-opacity-70 text-white">
            <CardContent className="p-6 flex flex-col items-center">
              <School className="w-10 h-10 mb-3 text-blue-400" />
              <h3 className="font-semibold text-lg">For Teachers</h3>
              <p className="text-sm text-gray-300 text-center">
                Manage classes, upload study materials, conduct tests,
                and track student progress easily.
              </p>
            </CardContent>
          </Card>
          <Card className="bg-black bg-opacity-70 text-white">
            <CardContent className="p-6 flex flex-col items-center">
              <BookOpen className="w-10 h-10 mb-3 text-blue-400" />
              <h3 className="font-semibold text-lg">For Admins</h3>
              <p className="text-sm text-gray-300 text-center">
                Monitor the whole system, approve admissions, manage staff,
                publish notices, and oversee results.
              </p>
            </CardContent>
          </Card>
        </div>
      </section>

      {/* ABOUT SECTION */}
      <section className="grid grid-cols-1 md:grid-cols-2 gap-8 p-16 items-center bg-black">
        <div>
          <h2 className="text-3xl font-bold mb-4">Why EduSync-360?</h2>
          <p className="text-gray-300">
            EduSync-360 is an all-in-one educational management system
            that connects students, teachers, and administrators on a
            single platform. From admissions to results, everything is
            digitized to save time and improve productivity.
          </p>
        </div>
        <img
          src="https://images.unsplash.com/photo-1606761568499-6d2451b23c57?auto=format&fit=crop&w=1600&q=80"
          alt="EduSync Learning"
          className="rounded-lg shadow-lg"
        />
      </section>

      {/* NEWS & EVENTS */}
      <section className="bg-blue-50 text-black p-16">
        <h2 className="text-2xl font-bold mb-6">Latest Updates</h2>
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
          <Card>
            <CardContent className="p-4">
              <h3 className="font-semibold">📢 New Admission Open</h3>
              <p className="text-sm text-gray-600">
                Register for the new academic year through our online admission form.
              </p>
              <Button className="mt-3 w-full">Apply Now</Button>
            </CardContent>
          </Card>
          <Card>
            <CardContent className="p-4">
              <h3 className="font-semibold">📊 Results Published</h3>
              <p className="text-sm text-gray-600">
                Check your performance in the latest tests and exams.
              </p>
              <Button className="mt-3 w-full">View Results</Button>
            </CardContent>
          </Card>
          <Card>
            <CardContent className="p-4">
              <h3 className="font-semibold">📅 Academic Calendar</h3>
              <Calendar mode="single" selected={date} onSelect={setDate} />
            </CardContent>
          </Card>
          <Card>
            <CardContent className="p-4">
              <h3 className="font-semibold">🎉 Student Achievements</h3>
              <p className="text-sm text-gray-600">
                Explore top-performing students and their success stories.
              </p>
              <Button className="mt-3 w-full">Know More</Button>
            </CardContent>
          </Card>
        </div>
      </section>

      {/* FOOTER */}
      <footer className="bg-black text-gray-400 py-12 px-10 grid grid-cols-1 md:grid-cols-3 gap-6">
        <div>
          <h3 className="font-bold text-white mb-3">Contact</h3>
          <p>Pune, India</p>
          <p>Email: support@edusync360.com</p>
          <p>Phone: +91 98765 43210</p>
        </div>
        <div>
          <h3 className="font-bold text-white mb-3">About Us</h3>
          <p>
            EduSync-360 is designed to make education management easier,
            faster, and more transparent for all stakeholders.
          </p>
        </div>
        <div>
          <h3 className="font-bold text-white mb-3">Quick Links</h3>
          <p><a href="/admission" className="hover:text-white">Admission</a></p>
          <p><a href="/results" className="hover:text-white">Results</a></p>
          <p><a href="/contact" className="hover:text-white">Contact</a></p>
        </div>
      </footer>
    </div>
  );
}
