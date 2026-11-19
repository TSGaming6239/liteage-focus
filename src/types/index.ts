export type Category = 
  | 'All'
  | 'Distractions'
  | 'Time Management'
  | 'Notes & Material'
  | 'Revision & Memory'
  | 'Exam Preparation';

export type Platform = 'Windows' | 'macOS' | 'Linux' | 'Android' | 'iOS' | 'Web' | 'Chrome / Edge Extension';

export interface AlternativeTool {
  id: string;
  name: string;
  tagline: string;
  pricingType: '100% Free' | 'Generous Free Tier' | 'Open Source' | '100% Free & Open Source';
  bestFor: string;
  websiteUrl: string;
  keyDifference: string;
}

export interface SetupStep {
  stepNumber: number;
  title: string;
  description: string;
  tip?: string;
}

export interface Solution {
  id: string;
  name: string;
  tagline: string;
  verifiedOfficialUrl: string;
  category: Category;
  pricingStatus: string;
  isCompletelyFree: boolean;
  freePlanDetails: string;
  paidPlanDetails?: string;
  platforms: Platform[];
  whyRecommended: string[];
  honestLimitations: string[];
  setupGuide: SetupStep[];
  alternatives: AlternativeTool[];
}

export interface Problem {
  id: string;
  title: string;
  shortSummary: string;
  category: Category;
  targetAudience: string;
  difficultyTag: 'High Priority' | 'Common Daily' | 'Critical Exam';
  commonSymptoms: string[];
  recommendedSolutionId: string;
}
