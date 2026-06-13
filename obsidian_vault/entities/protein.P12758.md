---
entity_id: "protein.P12758"
entity_type: "protein"
name: "udp"
source_database: "UniProt"
source_id: "P12758"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "udp b3831 JW3808"
---

# udp

`protein.P12758`

## Static

- Type: `protein`
- Source: `UniProt:P12758`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Catalyzes the reversible phosphorylytic cleavage of uridine to uracil and ribose-1-phosphate (PubMed:16751). Shows weak activity towards deoxyuridine and thymidine (PubMed:16751). The produced molecules are then utilized as carbon and energy sources or in the rescue of pyrimidine bases for nucleotide synthesis (Probable). {ECO:0000269|PubMed:16751, ECO:0000305}. Uridine phosphorylase (Udp) catalyzes the reversible phosphorolysis of uridine with the formation of ribose-1-phosphate and uracil . Udp belongs to the UP-1 subfamily of the nucleoside phosphorylase superfamily 1 . Udp is involved in utilization of nucleosides as a carbon and energy source and is part of a process that degrades "overflow" UMP nucleotides . The main activity of Udp is towards uracil ribonucleotides, but some activity is retained towards deoxyuridine and thymidine . The substrate specificity of the enzyme has been evaluated using a large set of modified nucleosides . The catalytic mechanism has been investigated . The Asp5 carboxyl group is important for catalysis . Various crystal structures of the enzyme alone or bound to substrates or inhibitors have been determined . The enzyme forms a toroidal homohexamer that can be described as a trimer of dimers. The presence of substrate induces conformational changes, closing the active site cleft...

## Biological Role

Catalyzes 5-fluorouridine:phosphate alpha-D-ribosyltransferase (reaction.R08229). Component of uridine phosphorylase (complex.ecocyc.URPHOS-CPLX).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the reversible phosphorylytic cleavage of uridine to uracil and ribose-1-phosphate (PubMed:16751). Shows weak activity towards deoxyuridine and thymidine (PubMed:16751). The produced molecules are then utilized as carbon and energy sources or in the rescue of pyrimidine bases for nucleotide synthesis (Probable). {ECO:0000269|PubMed:16751, ECO:0000305}.

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R08229|reaction.R08229]] `KEGG` `database` - via EC:2.4.2.3
- `is_component_of` --> [[complex.ecocyc.URPHOS-CPLX|complex.ecocyc.URPHOS-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b3831|gene.b3831]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P12758`
- `KEGG:ecj:JW3808;eco:b3831;ecoc:C3026_20730;`
- `GeneID:86861936;86948517;948987;`
- `GO:GO:0004850; GO:0005524; GO:0005829; GO:0006218; GO:0006974; GO:0030955; GO:0032991; GO:0042802; GO:0044206; GO:0046050`
- `EC:2.4.2.3`

## Notes

Uridine phosphorylase (UPase) (UrdPase) (EC 2.4.2.3)
