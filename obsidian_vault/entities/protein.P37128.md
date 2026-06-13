---
entity_id: "protein.P37128"
entity_type: "protein"
name: "nudK"
source_database: "UniProt"
source_id: "P37128"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nudK yffH b2467 JW2451"
---

# nudK

`protein.P37128`

## Static

- Type: `protein`
- Source: `UniProt:P37128`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Nucleoside diphosphate sugar hydrolase that hydrolyzes GDP-mannose as its preferred substrate, yielding GMP and mannose-1-phosphate. Can also hydrolyze the pyrophosphate bond of other sugar nucleotides such as IDP-ribose, GDP-glucose, and to a lesser extent, ADP-ribose, ADP-glucose and UDP-glucose. Shows no activity toward Nudix substrates FAD, CDP-ethanolamine, CDP-choline, NAD(+), diadenosine pentaphosphate, GTP, UTP, ATP, or CTP. {ECO:0000269|PubMed:16766526, ECO:0000269|PubMed:21638333}. The nudK gene product is a member of the ADP-ribose pyrophosphatase subfamily of the Nudix hydrolases. The enzyme has GDP-mannose hydrolase activity and prefers purine over pyrimidine nucleotide sugars as substrates . NudK was described to be either a homotrimer or a homodimer in solution. A crystal structure has been solved at 2.4 Å resolution . Additional crystal structures show the enzyme in a domain-swapped dimer conformation . Residues important for metal binding and catalytic activity were confirmed by site-directed mutagenesis . Deletion of nudK does not affect biofilm formation . Overexpression of nudK suppresses the essentiality of EG12691-MONOMER "lapB", which encodes a protein involved in lipopolysaccharide (LPS) assembly . Review:

## Biological Role

Component of GDP-mannose hydrolase (complex.ecocyc.CPLX0-3971).

## Annotation

FUNCTION: Nucleoside diphosphate sugar hydrolase that hydrolyzes GDP-mannose as its preferred substrate, yielding GMP and mannose-1-phosphate. Can also hydrolyze the pyrophosphate bond of other sugar nucleotides such as IDP-ribose, GDP-glucose, and to a lesser extent, ADP-ribose, ADP-glucose and UDP-glucose. Shows no activity toward Nudix substrates FAD, CDP-ethanolamine, CDP-choline, NAD(+), diadenosine pentaphosphate, GTP, UTP, ATP, or CTP. {ECO:0000269|PubMed:16766526, ECO:0000269|PubMed:21638333}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3971|complex.ecocyc.CPLX0-3971]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2467|gene.b2467]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37128`
- `KEGG:ecj:JW2451;eco:b2467;ecoc:C3026_13685;`
- `GeneID:947072;`
- `GO:GO:0000287; GO:0005829; GO:0006753; GO:0019693; GO:0042803; GO:0052751`
- `EC:3.6.1.-`

## Notes

GDP-mannose pyrophosphatase (EC 3.6.1.-) (GDP-mannose hydrolase) (GDPMK)
