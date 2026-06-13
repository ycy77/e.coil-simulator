---
entity_id: "protein.P60651"
entity_type: "protein"
name: "speB"
source_database: "UniProt"
source_id: "P60651"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "speB b2937 JW2904"
---

# speB

`protein.P60651`

## Static

- Type: `protein`
- Source: `UniProt:P60651`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the formation of putrescine from agmatine. {ECO:0000269|PubMed:10527864}. Agmatinase (SpeB) catalyzes the hydrolysis of agmatine to yield urea and putrescine, the product of the PWY-40 pathway . Crystal stuctures of SpeB have been solved . While the enzyme was initially thought to be homodimeric in solution , the crystal structures and gel filtration data agree on a homohexameric quarternary structure . One molecule of Mn2+ is present per SpeB monomer . The His163Phe , Asp153Asn , His126Asn, His151Asn and Glu174Ala mutations leads to loss of activity. Based on the structural and mutant data, a catalytic mechanism was proposed . Agmatinase activity is induced by the presence of its substrate, agmatine , as well as L-arginine . Experiments determining regulation of agmatinase activity by cAMP yielded contradictory results . later showed that the effect of cAMP on SpeB expression is indirect. Agmatinase synthesis is also controlled by nitrogen availability . The EG11291-MONOMER appears to enhance expression of agmatinase . A strain lacking the polyamines putrescine, spermidine and cadaverine due to deletion of speA, speB, speC, speD and cadA has a reduced growth rate compared to wild type. The presence of the rpsL9 (streptomycin resistance) allele leads to a requirement for polyamines for growth...

## Biological Role

Catalyzes agmatine amidinohydrolase (reaction.R01157). Component of agmatinase (complex.ecocyc.AGMATIN-CPLX).

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Catalyzes the formation of putrescine from agmatine. {ECO:0000269|PubMed:10527864}.

## Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R01157|reaction.R01157]] `KEGG` `database` - via EC:3.5.3.11
- `is_component_of` --> [[complex.ecocyc.AGMATIN-CPLX|complex.ecocyc.AGMATIN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2937|gene.b2937]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P60651`
- `KEGG:ecj:JW2904;eco:b2937;`
- `GeneID:86861026;89517749;947715;`
- `GO:GO:0005829; GO:0008295; GO:0008783; GO:0030145; GO:0033389; GO:0042802`
- `EC:3.5.3.11`

## Notes

Agmatinase (EC 3.5.3.11) (Agmatine ureohydrolase) (AUH)
