import React from 'react';
import { Problem, Solution } from '../types';
import { CompatibilityBadge } from '../components/CompatibilityBadge';
import { 
  ArrowLeft, 
  Sparkles, 
  CheckCircle2, 
  ExternalLink, 
  Bookmark, 
  AlertTriangle, 
  ArrowRight, 
  Layers,
  ChevronRight,
  ShieldCheck,
  Check
} from 'lucide-react';

interface ProblemPageProps {
  problem: Problem;
  solution: Solution;
  onNavigateHome: () => void;
  onNavigateToSolution: (solutionId: string) => void;
  isSaved: boolean;
  onToggleSave: (problemId: string, e: React.MouseEvent) => void;
}

export const ProblemPage: React.FC<ProblemPageProps> = ({
  problem,
  solution,
  onNavigateHome,
  onNavigateToSolution,
  isSaved,
  onToggleSave,
}) => {
  return (
    <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8 sm:py-12 space-y-10">
      
      {/* Breadcrumb & Back navigation */}
      <div className="flex items-center justify-between">
        <button
          onClick={onNavigateHome}
          className="inline-flex items-center gap-2 text-sm font-medium text-slate-600 hover:text-blue-600 hover:bg-white px-3 py-1.5 rounded-lg border border-transparent hover:border-slate-200 transition-all"
        >
          <ArrowLeft className="w-4 h-4" />
          <span>Back to Explore</span>
        </button>

        <div className="flex items-center gap-2 text-xs text-slate-400">
          <span className="hover:text-slate-600 cursor-pointer" onClick={onNavigateHome}>Home</span>
          <ChevronRight className="w-3.5 h-3.5" />
          <span className="text-slate-600 font-medium">{problem.category}</span>
        </div>
      </div>

      {/* Problem Header Section */}
      <div className="bg-white border border-slate-200 rounded-3xl p-6 sm:p-8 shadow-sm">
        <div className="flex flex-wrap items-center justify-between gap-3 mb-4">
          <div className="flex items-center gap-2">
            <span className="px-3 py-1 rounded-full text-xs font-semibold bg-blue-50 text-blue-700 border border-blue-200">
              {problem.category}
            </span>
            <span className="px-3 py-1 rounded-full text-xs font-medium bg-slate-100 text-slate-600">
              {problem.targetAudience}
            </span>
          </div>

          <button
            onClick={(e) => onToggleSave(problem.id, e)}
            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-semibold border transition-all ${
              isSaved
                ? 'bg-blue-50 text-blue-700 border-blue-200'
                : 'bg-white text-slate-700 border-slate-200 hover:bg-slate-50'
            }`}
          >
            <Bookmark className={`w-3.5 h-3.5 ${isSaved ? 'fill-blue-600 text-blue-600' : ''}`} />
            <span>{isSaved ? 'Saved to My Focus' : 'Save Solution'}</span>
          </button>
        </div>

        <h1 className="text-2xl sm:text-3xl font-extrabold text-slate-900 leading-tight">
          {problem.title}
        </h1>

        <p className="mt-3 text-base text-slate-600 leading-relaxed">
          {problem.shortSummary}
        </p>

        {/* Common Symptoms breakdown */}
        <div className="mt-6 pt-5 border-t border-slate-100">
          <h4 className="text-xs font-bold uppercase tracking-wider text-slate-400 mb-2.5">
            Common Student Struggles (From Week 1 Field Interviews):
          </h4>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs text-slate-700">
            {problem.commonSymptoms.map((symptom, idx) => (
              <div key={idx} className="flex items-start gap-2 bg-slate-50 p-2.5 rounded-xl border border-slate-100">
                <span className="text-amber-500 font-bold mt-0.5">•</span>
                <span className="italic leading-normal">"{symptom}"</span>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Main Recommended Tool Section (Follows Week 1 Sketch) */}
      <div className="relative">
        <div className="flex items-center justify-between mb-4">
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 rounded-lg bg-blue-600 text-white flex items-center justify-center">
              <Sparkles className="w-4 h-4" />
            </div>
            <div>
              <h2 className="text-xl font-bold text-slate-900">Our Primary Recommendation</h2>
              <p className="text-xs text-slate-500">Researched & tested to give students 1 verified solution</p>
            </div>
          </div>
          <span className="hidden sm:inline-flex items-center gap-1 text-xs font-semibold text-emerald-700 bg-emerald-50 px-3 py-1 rounded-full border border-emerald-200">
            <CheckCircle2 className="w-3.5 h-3.5" />
            Vetted for Student Budgets
          </span>
        </div>

        {/* Highlight Card */}
        <div className="bg-gradient-to-b from-white to-blue-50/20 border-2 border-blue-500/80 rounded-3xl p-6 sm:p-8 shadow-md">
          
          {/* Top row */}
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-6 border-b border-slate-100">
            <div>
              <div className="flex items-center gap-3">
                <h3 className="text-2xl sm:text-3xl font-extrabold text-slate-900">
                  {solution.name}
                </h3>
                <span className="inline-flex items-center gap-1 px-3 py-1 rounded-full text-xs font-bold bg-emerald-100 text-emerald-800">
                  <CheckCircle2 className="w-3 h-3" />
                  {solution.pricingStatus}
                </span>
              </div>
              <p className="text-sm sm:text-base text-slate-600 mt-1 max-w-2xl">
                {solution.tagline}
              </p>
            </div>

            <div className="shrink-0 flex items-center gap-2">
              <a
                href={solution.verifiedOfficialUrl}
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center gap-1.5 px-4 py-2.5 rounded-xl text-xs font-semibold bg-white border border-slate-300 text-slate-700 hover:bg-slate-50 hover:border-slate-400 transition-colors shadow-sm"
              >
                <span>Visit Official Site</span>
                <ExternalLink className="w-3.5 h-3.5" />
              </a>
            </div>
          </div>

          {/* Compatibility Platform Row */}
          <div className="py-4 border-b border-slate-100 flex flex-wrap items-center gap-2">
            <span className="text-xs font-semibold text-slate-500 mr-2">Supported Devices:</span>
            {solution.platforms.map((platform) => (
              <CompatibilityBadge key={platform} platform={platform} />
            ))}
          </div>

          {/* Why We Recommend It & Limitations 2-Column Grid */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6 py-6">
            
            {/* Left: Why we recommend it */}
            <div className="space-y-3">
              <h4 className="text-sm font-bold text-slate-900 flex items-center gap-2">
                <ShieldCheck className="w-4 h-4 text-blue-600" />
                Why We Recommend It
              </h4>
              <ul className="space-y-2">
                {solution.whyRecommended.map((point, idx) => (
                  <li key={idx} className="flex items-start gap-2.5 text-xs sm:text-sm text-slate-700">
                    <Check className="w-4 h-4 text-emerald-600 shrink-0 mt-0.5" />
                    <span>{point}</span>
                  </li>
                ))}
              </ul>
            </div>

            {/* Right: Limitations */}
            <div className="space-y-3 bg-amber-50/50 p-4 rounded-2xl border border-amber-200/60">
              <h4 className="text-sm font-bold text-amber-900 flex items-center gap-2">
                <AlertTriangle className="w-4 h-4 text-amber-600" />
                Important Limitations to Know
              </h4>
              <ul className="space-y-2">
                {solution.honestLimitations.map((lim, idx) => (
                  <li key={idx} className="flex items-start gap-2 text-xs text-amber-800">
                    <span className="text-amber-600 font-bold mt-0.5">•</span>
                    <span>{lim}</span>
                  </li>
                ))}
              </ul>
            </div>

          </div>

          {/* Primary Action to Screen 3 */}
          <div className="pt-6 border-t border-slate-100 flex flex-col sm:flex-row items-center justify-between gap-4">
            <div className="text-xs text-slate-500">
              Want step-by-step installation instructions and detailed device walkthroughs?
            </div>

            <button
              onClick={() => onNavigateToSolution(solution.id)}
              className="w-full sm:w-auto bg-blue-600 hover:bg-blue-700 text-white font-bold px-6 py-3 rounded-xl text-sm transition-all shadow-sm shadow-blue-500/20 flex items-center justify-center gap-2 group"
            >
              <span>View Full Setup Guide & Details</span>
              <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
            </button>
          </div>

        </div>
      </div>

      {/* Alternative Solutions Section */}
      <div className="space-y-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <Layers className="w-5 h-5 text-slate-600" />
            <h3 className="text-lg font-bold text-slate-900">Alternative Solutions</h3>
          </div>
          <span className="text-xs text-slate-500">If the primary recommendation does not fit your device</span>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          {solution.alternatives.map((alt) => (
            <div
              key={alt.id}
              className="bg-white border border-slate-200 rounded-2xl p-5 hover:border-slate-300 transition-all flex flex-col justify-between"
            >
              <div>
                <div className="flex items-center justify-between gap-2 mb-2">
                  <h4 className="font-bold text-slate-900 text-base">{alt.name}</h4>
                  <span className="text-[11px] font-medium bg-slate-100 text-slate-700 px-2 py-0.5 rounded">
                    {alt.pricingType}
                  </span>
                </div>
                <p className="text-xs text-slate-600 mb-3">{alt.tagline}</p>
                <div className="p-3 bg-slate-50 rounded-xl text-xs text-slate-700 space-y-1">
                  <p><strong className="text-slate-900">Best for:</strong> {alt.bestFor}</p>
                  <p><strong className="text-slate-900">Key difference:</strong> {alt.keyDifference}</p>
                </div>
              </div>

              <div className="mt-4 pt-3 border-t border-slate-100 flex items-center justify-between">
                <a
                  href={alt.websiteUrl}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-xs font-semibold text-blue-600 hover:text-blue-700 inline-flex items-center gap-1"
                >
                  <span>Visit website</span>
                  <ExternalLink className="w-3 h-3" />
                </a>
              </div>
            </div>
          ))}
        </div>
      </div>

    </div>
  );
};
