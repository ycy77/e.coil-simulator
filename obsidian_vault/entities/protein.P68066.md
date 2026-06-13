---
entity_id: "protein.P68066"
entity_type: "protein"
name: "grcA"
source_database: "UniProt"
source_id: "P68066"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "grcA yfiD b2579 JW2563"
---

# grcA

`protein.P68066`

## Static

- Type: `protein`
- Source: `UniProt:P68066`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Acts as a radical domain for damaged PFL and possibly other radical proteins. {ECO:0000269|PubMed:11444864}. GrcA is a small (14 kDa) glycyl radical enzyme (GRE) that can restore activity of oxygen-damaged PYRUVFORMLY-CPLX pyruvate formate-lyase (PFL). The relatively stable glycyl radical of PFL, which is essential for catalysis, is sensitive to OXYGEN-MOLECULE . Destruction of the glycyl radical by oxygen results in cleavage of the 85 kDa polypeptide to 83 kDa and a 3 kDa fragment and consequent inactivation of the enzyme . A solution structure of GrcA shows a flexible N-terminal domain followed by a C-terminal region with high amino acid sequence similarity to the glycyl radical domain of PFL . GrcA forms a complex with oxygen-damaged PFL enzyme and displaces the damaged C-terminal glycyl radical domain . After activation by PFLACTENZ-MONOMER (PflA), the PFL-GrcA complex has full pyruvate-formate lyase activity both in vitro and in vivo . In an arcA mutant under microaerobic conditions, GrcA contributes 18% of the flux through the pyruvate formate-lyase reaction . Residue Gly102 is predicted to be the glycyl radical site in GrcA and is necessary for restoring PflB activity . Lower intracellular pH increases both grcA expression and the extent of glycyl radical formation by PflA. ADHE-CPLX AdhE does not appear to deactivate GrcA...

## Biological Role

Component of PFL-GrcA complex (complex.ecocyc.CPLX0-9871).

## Annotation

FUNCTION: Acts as a radical domain for damaged PFL and possibly other radical proteins. {ECO:0000269|PubMed:11444864}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-9871|complex.ecocyc.CPLX0-9871]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2579|gene.b2579]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P68066`
- `KEGG:ecj:JW2563;eco:b2579;ecoc:C3026_14290;`
- `GeneID:93774507;947068;`
- `GO:GO:0005737; GO:0005829; GO:0006950; GO:0008861`

## Notes

Autonomous glycyl radical cofactor
