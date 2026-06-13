---
entity_id: "protein.P0AEI6"
entity_type: "protein"
name: "nudJ"
source_database: "UniProt"
source_id: "P0AEI6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nudJ ymfB b1134 JW1120"
---

# nudJ

`protein.P0AEI6`

## Static

- Type: `protein`
- Source: `UniProt:P0AEI6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the hydrolysis of 4-amino-2-methyl-5-hydroxymethylpyrimidine pyrophosphate (HMP-PP) to 4-amino-2-methyl-5-hydroxymethylpyrimidine phosphate (HMP-P), and hydrolysis of thiamine pyrophosphate (TPP) to thiamine monophosphate (TMP). Can hydrolyze other substrates such as MeO-HMP-PP, CF(3)-HMP-PP and MeO-TPP. Is also a non-specific nucleoside tri- and diphosphatase that releases inorganic orthophosphate. {ECO:0000269|PubMed:15292217, ECO:0000269|PubMed:16766526}. The nudJ gene product is a member of the Nudix hydrolase superfamily. Unlike the other Nudix nucleoside triphosphatases in E. coli, the product of the reaction is phosphate instead of pyrophosphate. NudJ is a promiscuous enzyme with no preference for deoxyribose or ribose, and nucleoside di- and tri-phosphates serve as substrates equally. The enzyme is a monomer in solution . NudJ also contributes to the production of dimethylallyl phosphate, which is the substrate for UBIX-MONOMER UbiX-catalyzed generation of the prFMN cofactor in ubiquinone biosynthesis . Crystal structures of NudJ have been solved. Together with kinetic data for active site mutants, they provide insight into the catalytic mechanism of the enzyme . Overexpression of NudJ from a multicopy plasmid leads to resistance to the HMP (4-amino-2-methyl-5-hydroxymethylpyrimidine) analog bacimethrin (MeO-HMP)...

## Biological Role

Catalyzes GUANOSINE-DIPHOSPHATASE-RXN (reaction.ecocyc.GUANOSINE-DIPHOSPHATASE-RXN), RXN0-3542 (reaction.ecocyc.RXN0-3542), RXN0-3543 (reaction.ecocyc.RXN0-3543), RXN0-7309 (reaction.ecocyc.RXN0-7309). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00740` Riboflavin metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the hydrolysis of 4-amino-2-methyl-5-hydroxymethylpyrimidine pyrophosphate (HMP-PP) to 4-amino-2-methyl-5-hydroxymethylpyrimidine phosphate (HMP-P), and hydrolysis of thiamine pyrophosphate (TPP) to thiamine monophosphate (TMP). Can hydrolyze other substrates such as MeO-HMP-PP, CF(3)-HMP-PP and MeO-TPP. Is also a non-specific nucleoside tri- and diphosphatase that releases inorganic orthophosphate. {ECO:0000269|PubMed:15292217, ECO:0000269|PubMed:16766526}.

## Pathways

- `eco00740` Riboflavin metabolism (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.GUANOSINE-DIPHOSPHATASE-RXN|reaction.ecocyc.GUANOSINE-DIPHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-3542|reaction.ecocyc.RXN0-3542]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-3543|reaction.ecocyc.RXN0-3543]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7309|reaction.ecocyc.RXN0-7309]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b1134|gene.b1134]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEI6`
- `KEGG:ecj:JW1120;eco:b1134;ecoc:C3026_06820;`
- `GeneID:75203720;945689;`
- `GO:GO:0002145; GO:0004787; GO:0016462; GO:0017110; GO:0017111`
- `EC:3.6.1.-`

## Notes

Phosphatase NudJ (EC 3.6.1.-)
