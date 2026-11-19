import React from 'react';
import { Problem, Solution } from '../types';
import { CompatibilityBadge } from '../components/CompatibilityBadge';
import { 
  ArrowLeft, 
  ExternalLink, 
  Bookmark, 
  CheckCircle2, 
  AlertTriangle, 
  Lightbulb, 
  Layers,
  ChevronRight
} from 'lucide-react';

interface SolutionDetailPageProps {
  solution: Solution;
  relatedProblem?: Problem;
  onNavigateBackToProblem: () => void;
  onNavigateHome: () => void;
  isSaved: boolean;
  onToggleSave: (e: React.MouseEvent) => void;
}

export const SolutionDetailPage: React.FC<SolutionDetailPageProps> = ({
  solution,
  relatedProblem,
  onNavigateBackToProblem,
  onNavigateHome,
  isSaved,
  onToggleSave,
}) => {
  return (
    <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8 sm:py-12 space-y-10">
      
      {/* Breadcrumb & Back navigation */}
      <div className="flex items-center justify-between">
        <button
          onClick={onNavigateBackToProblem}
          className="inline-flex items-center gap-2 text-sm font-medium text-slate-600 hover:text-blue-600 hover:bg-white px-3 py-1.5 rounded-lg border border-transparent hover:border-slate-200 transition-all"
        >
          <ArrowLeft className="w-4 h-4" />
          <span>Back to Problem</span>
        </button>

        <div className="flex items-center gap-2 text-xs text-slate-400">
          <span className="hover:text-slate-600 cursor-pointer" onClick={onNavigateHome}>Home</span>
          <ChevronRight className="w-3.5 h-3.5" />
          <span className="hover:text-slate-600 cursor-pointer" onClick={onNavigateBackToProblem}>
            {relatedProblem ? relatedProblem.category : 'Problem'}
          </span>
          <ChevronRight className="w-3.5 h-3.5" />
          <span className="text-slate-600 font-medium">{solution.name} Guide</span>
        </div>
      </div>

      {/* Main Solution Header */}
      <div className="bg-white border border-slate-200 rounded-3xl p-6 sm:p-8 shadow-sm">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-6 pb-6 border-b border-slate-100">
          <div className="space-y-2">
            <div className="flex flex-wrap items-center gap-2.5">
              <span className="px-3 py-1 rounded-full text-xs font-bold bg-blue-50 text-blue-700 border border-blue-200">
                Primary Recommendation
              </span>
              <span className="px-3 py-1 rounded-full text-xs font-semibold bg-emerald-50 text-emerald-800 border border-emerald-200">
                {solution.pricingStatus}
              </span>
            </div>

            <h1 className="text-2xl sm:text-4xl font-extrabold text-slate-900 tracking-tight">
              {solution.name}
            </h1>
            
            <p className="text-sm sm:text-base text-slate-600 max-w-2xl leading-relaxed">
              {solution.tagline}
            </p>
          </div>

          {/* Action Buttons */}
          <div className="flex flex-wrap items-center gap-3">
            <a
              href={solution.verifiedOfficialUrl}
              target="_blank"
              rel="noopener noreferrer"
              className="bg-blue-600 hover:bg-blue-700 text-white font-bold px-5 py-3 rounded-xl text-sm transition-all shadow-sm shadow-blue-500/20 flex items-center gap-2"
            >
              <span>Open Official Website</span>
              <ExternalLink className="w-4 h-4" />
            </a>

            <button
              onClick={onToggleSave}
              className={`p-3 rounded-xl border transition-all flex items-center justify-center ${
                isSaved
                  ? 'bg-blue-50 text-blue-600 border-blue-200'
                  : 'bg-white text-slate-700 border-slate-200 hover:bg-slate-50'
              }`}
              title={isSaved ? 'Saved in My Focus' : 'Save to My Focus'}
            >
              <Bookmark className={`w-5 h-5 ${isSaved ? 'fill-blue-600 text-blue-600' : ''}`} />
            </button>
          </div>
        </div>

        {/* Device & Platform Compatibility Matrix */}
        <div className="pt-6">
          <h4 className="text-xs font-bold uppercase tracking-wider text-slate-400 mb-3">
            Supported Operating Systems & Devices
          </h4>
          <div className="flex flex-wrap items-center gap-2">
            {solution.platforms.map((platform) => (
              <CompatibilityBadge key={platform} platform={platform} size="md" />
            ))}
          </div>
        </div>
      </div>

      {/* Pricing & Limitations Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        
        {/* Free Plan Transparency */}
        <div className="bg-emerald-50/40 border border-emerald-200/80 rounded-3xl p-6 sm:p-7 space-y-3">
          <div className="flex items-center gap-2 text-emerald-800">
            <CheckCircle2 className="w-5 h-5 text-emerald-600" />
            <h3 className="text-base font-bold text-slate-900">100% Free Plan Transparency</h3>
          </div>
          <p className="text-xs sm:text-sm text-slate-700 leading-relaxed">
            {solution.freePlanDetails}
          </p>
          <div className="pt-3 border-t border-emerald-200/60 text-xs text-emerald-800 font-medium">
            ✓ No mandatory credit card or trial period expiration.
          </div>
        </div>

        {/* Honest Limitations */}
        <div className="bg-amber-50/40 border border-amber-200/80 rounded-3xl p-6 sm:p-7 space-y-3">
          <div className="flex items-center gap-2 text-amber-900">
            <AlertTriangle className="w-5 h-5 text-amber-600" />
            <h3 className="text-base font-bold text-slate-900">Limitations & Things to Note</h3>
          </div>
          <ul className="space-y-2 text-xs sm:text-sm text-slate-700">
            {solution.honestLimitations.map((lim, idx) => (
              <li key={idx} className="flex items-start gap-2">
                <span className="text-amber-600 font-bold mt-0.5">•</span>
                <span>{lim}</span>
              </li>
            ))}
          </ul>
        </div>

      </div>

      {/* Step-by-Step Practical Usage Guide */}
      <div className="bg-white border border-slate-200 rounded-3xl p-6 sm:p-8 shadow-sm space-y-6">
        <div className="border-b border-slate-100 pb-4">
          <div className="inline-flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-blue-600 mb-1">
            <Lightbulb className="w-4 h-4" />
            <span>Practical Implementation Guide</span>
          </div>
          <h2 className="text-xl sm:text-2xl font-bold text-slate-900">
            How to Set Up & Use {solution.name} for Your Studies
          </h2>
          <p className="text-xs sm:text-sm text-slate-500 mt-1">
            Follow these 4 clear steps to integrate this solution directly into your daily routine.
          </p>
        </div>

        <div className="space-y-6">
          {solution.setupGuide.map((step) => (
            <div 
              key={step.stepNumber}
              className="flex items-start gap-4 p-4 sm:p-5 rounded-2xl bg-slate-50/80 border border-slate-200/60 hover:bg-slate-50 transition-colors"
            >
              <div className="w-9 h-9 rounded-xl bg-blue-600 text-white font-bold flex items-center justify-center shrink-0 text-sm shadow-sm">
                {step.stepNumber}
              </div>

              <div className="space-y-1.5 flex-1">
                <h4 className="text-sm sm:text-base font-bold text-slate-900">
                  {step.title}
                </h4>
                <p className="text-xs sm:text-sm text-slate-600 leading-relaxed">
                  {step.description}
                </p>
                {step.tip && (
                  <div className="mt-2.5 inline-flex items-start gap-1.5 text-xs text-blue-800 bg-blue-50 px-3 py-1.5 rounded-lg border border-blue-100">
                    <span className="font-bold text-blue-600">Student Tip:</span>
                    <span>{step.tip}</span>
                  </div>
                )}
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Comparison with Alternatives */}
      <div className="space-y-4">
        <div className="flex items-center justify-between">
          <div>
            <h3 className="text-lg font-bold text-slate-900 flex items-center gap-2">
              <Layers className="w-5 h-5 text-slate-600" />
              <span>How {solution.name} Compares to Alternatives</span>
            </h3>
            <p className="text-xs text-slate-500 mt-0.5">
              Why we picked {solution.name} over other popular tools
            </p>
          </div>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          {solution.alternatives.map((alt) => (
            <div
              key={alt.id}
              className="bg-white border border-slate-200 rounded-2xl p-5 space-y-3"
            >
              <div className="flex items-center justify-between">
                <h4 className="font-bold text-slate-900 text-base">{alt.name}</h4>
                <span className="text-[11px] font-medium bg-slate-100 text-slate-700 px-2 py-0.5 rounded">
                  {alt.pricingType}
                </span>
              </div>
              <p className="text-xs text-slate-600">{alt.tagline}</p>

              <div className="p-3 bg-slate-50 rounded-xl text-xs space-y-1 border border-slate-100">
                <p className="text-slate-700">
                  <strong className="text-slate-900">Best for:</strong> {alt.bestFor}
                </p>
                <p className="text-slate-700">
                  <strong className="text-slate-900">Difference:</strong> {alt.keyDifference}
                </p>
              </div>

              <div className="pt-2 flex justify-end">
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

      {/* Bottom Sticky-like Action Banner */}
      <div className="bg-slate-900 rounded-3xl p-6 sm:p-8 text-white flex flex-col sm:flex-row items-center justify-between gap-6">
        <div>
          <h3 className="text-lg font-bold">Ready to solve this problem?</h3>
          <p className="text-xs sm:text-sm text-slate-300 mt-1">
            Open {solution.name} directly and follow the 4-step setup guide above.
          </p>
        </div>

        <div className="flex items-center gap-3 w-full sm:w-auto">
          <button
            onClick={onNavigateBackToProblem}
            className="w-full sm:w-auto px-4 py-2.5 rounded-xl text-xs font-medium bg-slate-800 hover:bg-slate-700 text-slate-200 transition-colors"
          >
            Back to Problem
          </button>
          <a
            href={solution.verifiedOfficialUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="w-full sm:w-auto bg-blue-600 hover:bg-blue-500 text-white font-bold px-5 py-2.5 rounded-xl text-xs transition-all flex items-center justify-center gap-1.5 shadow-sm"
          >
            <span>Launch {solution.name}</span>
            <ExternalLink className="w-3.5 h-3.5" />
          </a>
        </div>
      </div>

    </div>
  );
};
