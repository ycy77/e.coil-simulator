---
entity_id: "protein.P0A8K1"
entity_type: "protein"
name: "psd"
source_database: "UniProt"
source_id: "P0A8K1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell membrane {ECO:0000255|HAMAP-Rule:MF_00662, ECO:0000269|PubMed:4598120}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_00662, ECO:0000269|PubMed:4598120}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "psd b4160 JW4121"
---

# psd

`protein.P0A8K1`

## Static

- Type: `protein`
- Source: `UniProt:P0A8K1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell membrane {ECO:0000255|HAMAP-Rule:MF_00662, ECO:0000269|PubMed:4598120}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_00662, ECO:0000269|PubMed:4598120}.

## Enriched Summary

FUNCTION: Catalyzes the formation of phosphatidylethanolamine (PtdEtn) from phosphatidylserine (PtdSer). Only decarboxylates the lipid-linked form of the serine moiety, and not serine alone or derivatives like phosphoserine or glycerophosphoserine. {ECO:0000255|HAMAP-Rule:MF_00662, ECO:0000269|PubMed:4598120}. This subunit contains the pyruvate prosthetic group . Phosphatidylserine decarboxylase catalyzes the formation of phosphatidylethanolamine, the most abundant phospholipid in E. coli membranes. Phosphatidylserine decarboxylase is one of a small class of enzymes that use a covalently bound pyruvoyl prosthetic group. The pyruvoyl group is thought to act analogously to pyridoxal phosphate cofactor by forming a Schiff base between its carbonyl residue and the amino group of the substrate and then serving as an electron sink to facilitate the decarboxylation. The pyruvoyl group is essential for catalytic activity and can be inactivated by carbonyl reagents . E. coli encodes two more members of this class of enzymes, CPLX0-2901 and SAMDECARB-CPLX. Pyruvoyl-containing enzymes are expressed as proenzymes, so-called "zymogens", which undergo a post-translational self-maturation/cleavage called serinolysis...

## Biological Role

Component of phosphatidylserine decarboxylase (complex.ecocyc.PHOSPHASERDECARB-DIMER).

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Catalyzes the formation of phosphatidylethanolamine (PtdEtn) from phosphatidylserine (PtdSer). Only decarboxylates the lipid-linked form of the serine moiety, and not serine alone or derivatives like phosphoserine or glycerophosphoserine. {ECO:0000255|HAMAP-Rule:MF_00662, ECO:0000269|PubMed:4598120}.

## Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.PHOSPHASERDECARB-DIMER|complex.ecocyc.PHOSPHASERDECARB-DIMER]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4160|gene.b4160]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A8K1`
- `KEGG:ecj:JW4121;eco:b4160;`
- `GeneID:75202394;948673;`
- `GO:GO:0004609; GO:0005886; GO:0006646; GO:0016540; GO:0031638; GO:0042803`
- `EC:4.1.1.65`

## Notes

Phosphatidylserine decarboxylase proenzyme (EC 4.1.1.65) [Cleaved into: Phosphatidylserine decarboxylase alpha chain; Phosphatidylserine decarboxylase beta chain]
