import React, { useState, useMemo } from 'react';
import { Problem, Solution, Category } from '../types';
import { SearchBar } from '../components/SearchBar';
import { CategoryPills } from '../components/CategoryPills';
import { ProblemCard } from '../components/ProblemCard';
import { Compass, Sparkles, Layers, ShieldCheck, ArrowRight } from 'lucide-react';

interface HomePageProps {
  problems: Problem[];
  solutions: Record<string, Solution>;
  onSelectProblem: (id: string) => void;
  savedProblemIds: string[];
  onToggleSave: (id: string, e: React.MouseEvent) => void;
}

export const HomePage: React.FC<HomePageProps> = ({
  problems,
  solutions,
  onSelectProblem,
  savedProblemIds,
  onToggleSave,
}) => {
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedCategory, setSelectedCategory] = useState<Category>('All');

  // Filter problems based on search query and category
  const filteredProblems = useMemo(() => {
    return problems.filter((problem) => {
      const matchesCategory =
        selectedCategory === 'All' || problem.category === selectedCategory;

      const q = searchQuery.toLowerCase().trim();
      const matchesSearch =
        q === '' ||
        problem.title.toLowerCase().includes(q) ||
        problem.shortSummary.toLowerCase().includes(q) ||
        problem.category.toLowerCase().includes(q) ||
        problem.targetAudience.toLowerCase().includes(q) ||
        problem.commonSymptoms.some((s) => s.toLowerCase().includes(q));

      return matchesCategory && matchesSearch;
    });
  }, [problems, selectedCategory, searchQuery]);

  // Featured sample problem from Shivendra's Week 1 interview #1
  const featuredProblem = problems.find((p) => p.id === 'laptop-distractions-youtube');

  return (
    <div className="space-y-12 sm:space-y-16">
      
      {/* Hero Section */}
      <section className="text-center pt-8 sm:pt-14 pb-4 max-w-4xl mx-auto px-4">
        
        {/* Pill Badge */}
        <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-blue-50 border border-blue-200/80 text-blue-700 text-xs font-semibold mb-6 shadow-sm">
          <Sparkles className="w-3.5 h-3.5 text-blue-600" />
          <span>Curated Free Digital Directory for Students</span>
        </div>

        {/* Main Heading */}
        <h1 className="text-3xl sm:text-5xl font-extrabold text-slate-900 tracking-tight leading-[1.15]">
          Find the right solution for <br className="hidden sm:inline" />
          <span className="text-blue-600">your specific problem.</span>
        </h1>

        {/* Subtitle */}
        <p className="mt-4 sm:mt-5 text-base sm:text-lg text-slate-600 max-w-2xl mx-auto leading-relaxed">
          No scattered Google searches. No paywalled traps. Just one verified, free-first solution for each academic and productivity obstacle.
        </p>

        {/* Search Bar */}
        <div className="mt-8 sm:mt-10">
          <SearchBar
            query={searchQuery}
            onChange={setSearchQuery}
            resultCount={filteredProblems.length}
          />
        </div>

        {/* Quick Suggestion Tags */}
        <div className="mt-4 flex flex-wrap items-center justify-center gap-2 text-xs text-slate-500">
          <span className="font-medium text-slate-400">Popular searches:</span>
          {['YouTube Distractions', 'School vs Coaching', 'Scattered PDFs', 'Active Recall', 'PYQs'].map((tag) => (
            <button
              key={tag}
              onClick={() => {
                if (tag === 'YouTube Distractions') setSearchQuery('distractions');
                else if (tag === 'School vs Coaching') setSearchQuery('coaching');
                else if (tag === 'Scattered PDFs') setSearchQuery('notes');
                else if (tag === 'Active Recall') setSearchQuery('revision');
                else if (tag === 'PYQs') setSearchQuery('PYQ');
              }}
              className="text-slate-600 hover:text-blue-600 hover:bg-blue-50 px-2 py-0.5 rounded-md transition-colors"
            >
              #{tag}
            </button>
          ))}
        </div>
      </section>

      {/* Featured Spotlight Card */}
      {featuredProblem && !searchQuery && selectedCategory === 'All' && (
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="bg-gradient-to-r from-blue-600 to-indigo-700 rounded-2xl p-6 sm:p-8 text-white shadow-lg relative overflow-hidden">
            <div className="relative z-10 max-w-3xl">
              <span className="inline-block text-[11px] font-bold uppercase tracking-wider bg-white/20 px-3 py-1 rounded-full mb-3 backdrop-blur-sm">
                Most Common Student Struggle
              </span>
              <h2 className="text-xl sm:text-2xl font-bold leading-snug">
                {featuredProblem.title}
              </h2>
              <p className="mt-2 text-sm sm:text-base text-blue-100 max-w-2xl leading-relaxed">
                Students need YouTube for lectures, but home feeds and shorts ruin their evening. Here is the verified 100% free solution.
              </p>
              
              <div className="mt-6 flex flex-wrap items-center gap-4">
                <button
                  onClick={() => onSelectProblem(featuredProblem.id)}
                  className="bg-white text-blue-700 hover:bg-blue-50 font-bold px-5 py-2.5 rounded-xl text-sm transition-all shadow-sm flex items-center gap-2"
                >
                  <span>View Verified Solution</span>
                  <ArrowRight className="w-4 h-4" />
                </button>
                <div className="flex items-center gap-2 text-xs text-blue-100">
                  <ShieldCheck className="w-4 h-4 text-emerald-300" />
                  <span>Recommended tool: <strong>LeechBlock NG</strong> (Free & Open Source)</span>
                </div>
              </div>
            </div>

            {/* Decorative background circle */}
            <div className="absolute -right-10 -bottom-10 w-64 h-64 bg-white/10 rounded-full blur-2xl pointer-events-none" />
          </div>
        </section>
      )}

      {/* Browse by Category Section */}
      <section id="explore-problems" className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 scroll-mt-24">
        <div className="flex items-center justify-between mb-4">
          <div>
            <h2 className="text-lg sm:text-xl font-bold text-slate-900 flex items-center gap-2">
              <Layers className="w-5 h-5 text-blue-600" />
              <span>Browse by Category</span>
            </h2>
            <p className="text-xs sm:text-sm text-slate-500 mt-0.5">
              Select an area to quickly filter student academic and productivity bottlenecks.
            </p>
          </div>
          {selectedCategory !== 'All' && (
            <button
              onClick={() => setSelectedCategory('All')}
              className="text-xs font-semibold text-blue-600 hover:text-blue-700 hover:underline"
            >
              Reset to All
            </button>
          )}
        </div>

        <CategoryPills
          selectedCategory={selectedCategory}
          onSelectCategory={setSelectedCategory}
        />
      </section>

      {/* Problems Grid Section */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between mb-6">
          <div>
            <h2 className="text-xl sm:text-2xl font-bold text-slate-900">
              {selectedCategory === 'All' ? 'Popular Student Problems' : `${selectedCategory} Problems`}
            </h2>
            <p className="text-xs sm:text-sm text-slate-500 mt-1">
              Showing {filteredProblems.length} {filteredProblems.length === 1 ? 'problem' : 'problems'} with vetted free solutions.
            </p>
          </div>
        </div>

        {filteredProblems.length === 0 ? (
          <div className="text-center py-16 bg-white border border-slate-200 rounded-2xl p-8 max-w-md mx-auto">
            <div className="w-12 h-12 bg-slate-100 rounded-full flex items-center justify-center mx-auto text-slate-400 mb-3">
              <Compass className="w-6 h-6" />
            </div>
            <h3 className="text-base font-bold text-slate-800">No matching problems found</h3>
            <p className="text-xs text-slate-500 mt-1.5 leading-relaxed">
              We couldn't find a problem matching "{searchQuery}". Try searching for generic terms like "distraction", "notes", "time", or clear your filter.
            </p>
            <button
              onClick={() => {
                setSearchQuery('');
                setSelectedCategory('All');
              }}
              className="mt-4 px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white text-xs font-medium rounded-xl transition-colors"
            >
              Clear Search & Show All
            </button>
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {filteredProblems.map((problem) => (
              <ProblemCard
                key={problem.id}
                problem={problem}
                solution={solutions[problem.recommendedSolutionId]}
                onSelect={onSelectProblem}
                isSaved={savedProblemIds.includes(problem.id)}
                onToggleSave={onToggleSave}
              />
            ))}
          </div>
        )}
      </section>

      {/* Why Liteage Focus Philosophy Banner */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="bg-slate-100/80 border border-slate-200/80 rounded-2xl p-6 sm:p-8">
          <div className="max-w-3xl">
            <h3 className="text-base sm:text-lg font-bold text-slate-900 mb-2">
              Why not just search Google or ask an AI?
            </h3>
            <p className="text-xs sm:text-sm text-slate-600 leading-relaxed">
              Google searches return sponsored affiliate blogs pushing costly tools. Generic AIs invent features or recommend software requiring credit cards. Liteage Focus hand-tests tools on actual student devices, verifies pricing limits, and presents one honest recommendation.
            </p>
          </div>
        </div>
      </section>

    </div>
  );
};
