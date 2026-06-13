---
entity_id: "protein.P21889"
entity_type: "protein"
name: "aspS"
source_database: "UniProt"
source_id: "P21889"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "aspS tls b1866 JW1855"
---

# aspS

`protein.P21889`

## Static

- Type: `protein`
- Source: `UniProt:P21889`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Catalyzes the attachment of L-aspartate to tRNA(Asp) in a two-step reaction: L-aspartate is first activated by ATP to form Asp-AMP and then transferred to the acceptor end of tRNA(Asp). Also mischarges tRNA(Asp) with D-aspartate, although it is a poor substrate (PubMed:10918062). {ECO:0000255|HAMAP-Rule:MF_00044, ECO:0000269|PubMed:10918062}. Aspartate—tRNA ligase (AspRS) is a member of the family of aminoacyl-tRNA synthetases, which interpret the genetic code by covalently linking amino acids to their specific tRNA molecules. The reaction is driven by ATP hydrolysis. AspRS belongs to the Class IIb aminoacyl-tRNA synthetases . The enzyme is a dimer in solution . Crystal structures of AspRS have been determined and allow modelling of specific interactions with the tRNA and the reaction mechanism . AspRS activity appears to be the target of processed CPD0-1129, which is an aspartyl adenylate analog . The tls-1 allele of aspS consists of a P555S mutation in the highly conserved proline residue of motif 3. It has no significant effect on substrate binding, but may affect the active site . Specific interactions of AspRS with tRNA(Asp) were deduced from the crystal structures and by mutagenesis of the tRNA substrate . The L45 loop within the OB-fold domain of AspRS appears to be responsible for anticodon recognition...

## Biological Role

Component of aspartate—tRNA ligase (complex.ecocyc.ASPS-CPLX).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

FUNCTION: Catalyzes the attachment of L-aspartate to tRNA(Asp) in a two-step reaction: L-aspartate is first activated by ATP to form Asp-AMP and then transferred to the acceptor end of tRNA(Asp). Also mischarges tRNA(Asp) with D-aspartate, although it is a poor substrate (PubMed:10918062). {ECO:0000255|HAMAP-Rule:MF_00044, ECO:0000269|PubMed:10918062}.

## Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ASPS-CPLX|complex.ecocyc.ASPS-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1866|gene.b1866]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P21889`
- `KEGG:ecj:JW1855;eco:b1866;ecoc:C3026_10625;`
- `GeneID:946385;`
- `GO:GO:0003676; GO:0004815; GO:0005524; GO:0005829; GO:0006422`
- `EC:6.1.1.12`

## Notes

Aspartate--tRNA ligase (EC 6.1.1.12) (Aspartyl-tRNA synthetase) (AspRS)
