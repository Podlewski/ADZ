% Copyright (c) 2009 Jaroslaw Koszuk
%
% $Id$


\ProvidesClass{classrep}[2009/11/27 ICS Class Assignment Report]

\LoadClass[12pt,a4paper,authortitle]{mwart}
\usepackage[T1,plmath]{polski}
\usepackage{url}

\makeatletter

\def\studycycle#1{\gdef\@studycycle{#1}}
\def\@studycycle{\ClassError{classrep}{No \noexpand\studycycle given}{}}
\def\coursesemester#1{\gdef\@coursesemester{#1}}
\def\@coursesemester{\ClassError{classrep}{No \noexpand\coursesemester given}{}}
\def\coursename#1{\gdef\@coursename{#1}}
\def\@coursename{\ClassError{classrep}{No \noexpand\coursename given}{}}
\def\courseyear#1{\gdef\@courseyear{#1}}
\def\@courseyear{\ClassError{classrep}{No \noexpand\courseyear given}{}}
\def\courseteacher#1{\gdef\@courseteacher{#1}}
\def\@courseteacher{\ClassError{classrep}{No \noexpand\courseteacher given}{}}
\def\coursegroup#1{\gdef\@coursegroup{#1}}
\def\@coursegroup{\ClassError{classrep}{No \noexpand\coursegroup given}{}}

\newcommand\studentinfo[3][]{#2&#3&\texttt{#1}}

\newcommand\coursesemesterfield{semestr}
\newcommand\courseteacherfield{Prowadzący}

\newcommand\@typesetauthors{%
    {\large
      \begin{center}Autorzy:\end{center}
      \begin{tabular}[t]{lrl}%
        \strut\@author
      \end{tabular}\par}%
}
% \renewcommand{\and}{\\ \large\strut}

\newcommand\@typesettitle{{\LARGE \@title \par}}

\renewcommand{\@maketitle}{%
  \begin{titlepage}
  \null
  \noindent\strut\@studycycle\hfill\coursesemesterfield\ \@coursesemester
  \hrule{\hspace{\textwidth}}\\
  {\large\noindent\textbf{\@coursename\hfill\@courseyear}}\\
  \noindent\strut\courseteacherfield: \@courseteacher \hfill\@coursegroup
  \hrule{\hspace{\textwidth}}\\
  \vskip 3\baselineskip
  \begin{center}%
  \let \footnote \thanks
    \large
    \@typesettitle
    \vspace{375px}
    \@typesetauthors
  \par
  \end{center}%
  \end{titlepage}
  \setcounter{page}{2}
  \newpage
  }

