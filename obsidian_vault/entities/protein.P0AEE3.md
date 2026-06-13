---
entity_id: "protein.P0AEE3"
entity_type: "protein"
name: "degS"
source_database: "UniProt"
source_id: "P0AEE3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305|PubMed:11442831}; Single-pass membrane protein {ECO:0000305|PubMed:11442831}. Note=It is unclear how this protein is anchored to the inner membrane, programs predict a signal sequence, but replacing the N-terminal 26 residues with a known signal sequence gives a protein unable to fully complement a disruption mutant. {ECO:0000269|PubMed:11442831}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "degS hhoB htrH b3235 JW3204"
---

# degS

`protein.P0AEE3`

## Static

- Type: `protein`
- Source: `UniProt:P0AEE3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305|PubMed:11442831}; Single-pass membrane protein {ECO:0000305|PubMed:11442831}. Note=It is unclear how this protein is anchored to the inner membrane, programs predict a signal sequence, but replacing the N-terminal 26 residues with a known signal sequence gives a protein unable to fully complement a disruption mutant. {ECO:0000269|PubMed:11442831}.

## Enriched Summary

FUNCTION: A site-1 protease (S1P) that cleaves the peptide bond between 'Val-148' and 'Ser-149' in RseA. Part of a regulated intramembrane proteolysis (RIP) cascade. When heat shock or other environmental stresses disrupt protein folding in the periplasm, DegS senses the accumulation of unassembled outer membrane porins (OMP) and then initiates RseA (anti sigma-E factor) degradation by cleaving its periplasmic domain, making it a substrate for subsequent cleavage by RseP. This cascade ultimately leads to the sigma-E-driven expression of a variety of factors dealing with folding stress in the periplasm and OMP assembly. Required for basal and stress-induced degradation of RseA. {ECO:0000269|PubMed:10500101, ECO:0000269|PubMed:11442831, ECO:0000269|PubMed:12183368, ECO:0000269|PubMed:12183369, ECO:0000269|PubMed:12679035, ECO:0000269|PubMed:17360428, ECO:0000269|PubMed:17938245, ECO:0000269|PubMed:18945679, ECO:0000269|PubMed:19695325, ECO:0000269|PubMed:19706448}.

## Biological Role

Component of serine endoprotease (complex.ecocyc.CPLX0-8183).

## Annotation

FUNCTION: A site-1 protease (S1P) that cleaves the peptide bond between 'Val-148' and 'Ser-149' in RseA. Part of a regulated intramembrane proteolysis (RIP) cascade. When heat shock or other environmental stresses disrupt protein folding in the periplasm, DegS senses the accumulation of unassembled outer membrane porins (OMP) and then initiates RseA (anti sigma-E factor) degradation by cleaving its periplasmic domain, making it a substrate for subsequent cleavage by RseP. This cascade ultimately leads to the sigma-E-driven expression of a variety of factors dealing with folding stress in the periplasm and OMP assembly. Required for basal and stress-induced degradation of RseA. {ECO:0000269|PubMed:10500101, ECO:0000269|PubMed:11442831, ECO:0000269|PubMed:12183368, ECO:0000269|PubMed:12183369, ECO:0000269|PubMed:12679035, ECO:0000269|PubMed:17360428, ECO:0000269|PubMed:17938245, ECO:0000269|PubMed:18945679, ECO:0000269|PubMed:19695325, ECO:0000269|PubMed:19706448}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8183|complex.ecocyc.CPLX0-8183]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b3235|gene.b3235]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEE3`
- `KEGG:ecj:JW3204;eco:b3235;ecoc:C3026_17600;`
- `GeneID:93778751;947865;`
- `GO:GO:0004252; GO:0005886; GO:0006508; GO:0008233; GO:0008236; GO:0030288; GO:0042802; GO:0071218`
- `EC:3.4.21.107`

## Notes

Serine endoprotease DegS (EC 3.4.21.107) (Site-1 protease DegS) (S1P protease DegS) (Site-1-type intramembrane protease)
