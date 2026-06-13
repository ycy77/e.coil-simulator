---
entity_id: "protein.P06709"
entity_type: "protein"
name: "birA"
source_database: "UniProt"
source_id: "P06709"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "birA bioR dhbB b3973 JW3941"
---

# birA

`protein.P06709`

## Static

- Type: `protein`
- Source: `UniProt:P06709`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Acts both as a biotin--[acetyl-CoA-carboxylase] ligase and a biotin-operon repressor. In the presence of ATP, BirA activates biotin to form the BirA-biotinyl-5'-adenylate (BirA-bio-5'-AMP or holoBirA) complex. HoloBirA can either transfer the biotinyl moiety to the biotin carboxyl carrier protein (BCCP) subunit of acetyl-CoA carboxylase, or bind to the biotin operator site and inhibit transcription of the operon. {ECO:0000255|HAMAP-Rule:MF_00978, ECO:0000269|PubMed:12527300, ECO:0000269|PubMed:2667763, ECO:0000269|PubMed:6129246, ECO:0000269|PubMed:8003500}. BirA is a bifunctional protein that exhibits biotin ligase activity and also acts as the DNA binding transcriptional repressor of the biotin operon . The effector of BirA transcriptional repression activity, biotinyl-5'-adenylate (bio-5'-AMP), is also a substrate in the BirA-mediated biotinylation of the biotin carboxyl carrier protein monomer (apoBCCP), and this relationship results in repression of the biotin operon when the abundance of apoBCCP (and therefore the cellular demand for biotin) is reduced . The enzymatic functions include the synthesis of the enzyme-bound biotinyl-5'-adenylate (bio-5'-AMP), and the transfer of the biotin from the adenylate to a lysine residue of the biotin carboxyl carrier protein (BCCP) of the acetyl-CoA-carboxylase...

## Biological Role

Catalyzes BIOTINLIG-RXN (reaction.ecocyc.BIOTINLIG-RXN). Component of BirA-biotinyl-5'-adenylate DNA-binding transcriptional repressor / biotin-[acetyl-CoA-carboxylase] ligase (complex.ecocyc.MONOMER-48). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00780` Biotin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Acts both as a biotin--[acetyl-CoA-carboxylase] ligase and a biotin-operon repressor. In the presence of ATP, BirA activates biotin to form the BirA-biotinyl-5'-adenylate (BirA-bio-5'-AMP or holoBirA) complex. HoloBirA can either transfer the biotinyl moiety to the biotin carboxyl carrier protein (BCCP) subunit of acetyl-CoA carboxylase, or bind to the biotin operator site and inhibit transcription of the operon. {ECO:0000255|HAMAP-Rule:MF_00978, ECO:0000269|PubMed:12527300, ECO:0000269|PubMed:2667763, ECO:0000269|PubMed:6129246, ECO:0000269|PubMed:8003500}.

## Pathways

- `eco00780` Biotin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (7)

- `catalyzes` --> [[reaction.ecocyc.BIOTINLIG-RXN|reaction.ecocyc.BIOTINLIG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.MONOMER-48|complex.ecocyc.MONOMER-48]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b0774|gene.b0774]] `RegulonDB` `S` - regulator=BirA; target=bioA; function=-
- `represses` --> [[gene.b0775|gene.b0775]] `RegulonDB` `S` - regulator=BirA; target=bioB; function=-
- `represses` --> [[gene.b0776|gene.b0776]] `RegulonDB` `S` - regulator=BirA; target=bioF; function=-
- `represses` --> [[gene.b0777|gene.b0777]] `RegulonDB` `S` - regulator=BirA; target=bioC; function=-
- `represses` --> [[gene.b0778|gene.b0778]] `RegulonDB` `S` - regulator=BirA; target=bioD; function=-

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3973|gene.b3973]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P06709`
- `KEGG:ecj:JW3941;eco:b3973;ecoc:C3026_21465;`
- `GeneID:948469;`
- `GO:GO:0000976; GO:0003676; GO:0003677; GO:0004077; GO:0005524; GO:0005737; GO:0006355; GO:0006768; GO:0009102; GO:0009374; GO:0017053; GO:0042803`
- `EC:6.3.4.15`

## Notes

Bifunctional ligase/repressor BirA (Biotin operon repressor) (Biotin--[acetyl-CoA-carboxylase] ligase) (EC 6.3.4.15) (Biotin--protein ligase) (Biotin-[acetyl-CoA carboxylase] synthetase)
