---
entity_id: "protein.P0ABQ0"
entity_type: "protein"
name: "coaBC"
source_database: "UniProt"
source_id: "P0ABQ0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "coaBC dfp b3639 JW5642"
---

# coaBC

`protein.P0ABQ0`

## Static

- Type: `protein`
- Source: `UniProt:P0ABQ0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes two sequential steps in the biosynthesis of coenzyme A. In the first step cysteine is conjugated to 4'-phosphopantothenate to form 4-phosphopantothenoylcysteine (PubMed:11278255, PubMed:12140293, PubMed:14686929). In the second step the latter compound is decarboxylated to form 4'-phosphopantotheine (PubMed:10922366, PubMed:11358972). {ECO:0000269|PubMed:10922366, ECO:0000269|PubMed:11278255, ECO:0000269|PubMed:11358972, ECO:0000269|PubMed:12140293, ECO:0000269|PubMed:14686929}. The dfp (coaBC) gene encodes an enzyme with two domains, each catalyzing one of two sequential reactions in the coenzyme A biosynthetic pathway . The C-terminal ("CoaB") domain of the protein confers phosphopantothenoylcysteine synthetase activity . When expressed separately, the CoaB domain forms dimers in solution. Point mutants in conserved residues have been generated and analyzed, and the existence of a 4'-phosphopantothenoyl-CMP intermediate of the two half reactions has been confirmed . Crystal structures of this domain have been solved, and a reaction mechanism has been proposed . Small molecule inhibitors have been designed and tested . The N-terminal ("CoaC") domain of the protein binds FMN and confers 4'-phosphopantothenoylcysteine decarboxylase activity . The domain can be expressed separately and forms dodecamers...

## Biological Role

Component of fused 4'-phosphopantothenoylcysteine decarboxylase and phosphopantothenoylcysteine synthetase (complex.ecocyc.CPLX0-341).

## Enriched Pathways

- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes two sequential steps in the biosynthesis of coenzyme A. In the first step cysteine is conjugated to 4'-phosphopantothenate to form 4-phosphopantothenoylcysteine (PubMed:11278255, PubMed:12140293, PubMed:14686929). In the second step the latter compound is decarboxylated to form 4'-phosphopantotheine (PubMed:10922366, PubMed:11358972). {ECO:0000269|PubMed:10922366, ECO:0000269|PubMed:11278255, ECO:0000269|PubMed:11358972, ECO:0000269|PubMed:12140293, ECO:0000269|PubMed:14686929}.

## Pathways

- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-341|complex.ecocyc.CPLX0-341]] `EcoCyc` `database` - EcoCyc component coefficient=12 | EcoCyc protcplxs.col coefficient=12

## Incoming Edges (1)

- `encodes` <-- [[gene.b3639|gene.b3639]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABQ0`
- `KEGG:ecj:JW5642;eco:b3639;ecoc:C3026_19720;`
- `GeneID:949047;`
- `GO:GO:0004632; GO:0004633; GO:0005829; GO:0010181; GO:0015937; GO:0015941; GO:0042802; GO:0046872; GO:0071513`
- `EC:4.1.1.36; 6.3.2.5`

## Notes

Coenzyme A biosynthesis bifunctional protein CoaBC (DNA/pantothenate metabolism flavoprotein) (Phosphopantothenoylcysteine synthetase/decarboxylase) (PPCS-PPCDC) [Includes: Phosphopantothenoylcysteine decarboxylase (PPC decarboxylase) (PPC-DC) (EC 4.1.1.36) (CoaC); Phosphopantothenate--cysteine ligase (EC 6.3.2.5) (CoaB) (Phosphopantothenoylcysteine synthetase) (PPC synthetase) (PPC-S)]
