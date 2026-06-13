---
entity_id: "complex.ecocyc.CPLX0-743"
entity_type: "complex"
name: "1-deoxy-D-xylulose-5-phosphate synthase"
source_database: "EcoCyc"
source_id: "CPLX0-743"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "DSXP"
---

# 1-deoxy-D-xylulose-5-phosphate synthase

`complex.ecocyc.CPLX0-743`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-743`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P77488|protein.P77488]]

## Enriched Summary

1-deoxyxylulose-5-phosphate synthase (Dxs) catalyzes the first, rate-limiting step in the methylerythritol phosphate pathway of isoprenoid biosynthesis, as well as feeding into the pyridoxal 5-phosphate and thiamine biosynthesis pathways . Dxs catalyzes the thiamine diphosphate (ThDP)-dependent reaction that condenses pyruvate and D-glyceraldehyde-3-phosphate (D-GAP) to yield the branch point metabolite 1-deoxy-D-xylulose 5-phosphate . The interaction of Dxs with its two substrates has been probed with atomic force microscopy single-molecule force spectroscopy (SMFS) . Catalysis occurs via a unique random sequential, preferred order mechanism . A pre-decarboxylation covalent intermediate (C2α-lactylThDP, LThDP) between ThDP and pyruvate is formed and stabilized in the absence of D-GAP; addition of D-GAP enhances (or "triggers") the rate of decarboxylation. A "gated" reaction mechanism involving the formation of a ternary complex with LThDP and D-GAP has been proposed . The role of the conformational dynamics of the enzyme during catalysis has been elucidated by hydrogen—deuterium exchange mass spectrometry . Chemical and biochemical characterization of D-GAP analogs and a variety of aliphatic aldehydes found that the aldehyde moiety of these small molecules activates decarboxylation of LThDP and possibly enables metabolic adaptations in response to chemical environments...

## Biological Role

Catalyzes DXS-RXN (reaction.ecocyc.DXS-RXN). Bound by Thiamin diphosphate (molecule.C00068).

## Annotation

1-deoxyxylulose-5-phosphate synthase (Dxs) catalyzes the first, rate-limiting step in the methylerythritol phosphate pathway of isoprenoid biosynthesis, as well as feeding into the pyridoxal 5-phosphate and thiamine biosynthesis pathways . Dxs catalyzes the thiamine diphosphate (ThDP)-dependent reaction that condenses pyruvate and D-glyceraldehyde-3-phosphate (D-GAP) to yield the branch point metabolite 1-deoxy-D-xylulose 5-phosphate . The interaction of Dxs with its two substrates has been probed with atomic force microscopy single-molecule force spectroscopy (SMFS) . Catalysis occurs via a unique random sequential, preferred order mechanism . A pre-decarboxylation covalent intermediate (C2α-lactylThDP, LThDP) between ThDP and pyruvate is formed and stabilized in the absence of D-GAP; addition of D-GAP enhances (or "triggers") the rate of decarboxylation. A "gated" reaction mechanism involving the formation of a ternary complex with LThDP and D-GAP has been proposed . The role of the conformational dynamics of the enzyme during catalysis has been elucidated by hydrogen—deuterium exchange mass spectrometry . Chemical and biochemical characterization of D-GAP analogs and a variety of aliphatic aldehydes found that the aldehyde moiety of these small molecules activates decarboxylation of LThDP and possibly enables metabolic adaptations in response to chemical environments . A structure of dimeric Dxs complexed with its coenzyme thiamine pyrophosphate has been determined to 2.4 Å resolution . Mutation of a conserved histidine residue to glutamine (H49Q) results in loss of catalytic activity . Mutants in other predicted active site residues have been analyzed , and residues involved in substrate binding have been identified . Overexpression of Dxs results in increased isopr

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.DXS-RXN|reaction.ecocyc.DXS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00068|molecule.C00068]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P77488|protein.P77488]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-743`
- `QSPROTEOME:QS00049588`

## Notes

2*protein.P77488
