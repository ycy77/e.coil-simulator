---
entity_id: "protein.P13001"
entity_type: "protein"
name: "bioH"
source_database: "UniProt"
source_id: "P13001"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "bioH bioB b3412 JW3375"
---

# bioH

`protein.P13001`

## Static

- Type: `protein`
- Source: `UniProt:P13001`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}.

## Enriched Summary

FUNCTION: The physiological role of BioH is to remove the methyl group introduced by BioC when the pimeloyl moiety is complete. It allows to synthesize pimeloyl-ACP via the fatty acid synthetic pathway through the hydrolysis of the ester bonds of pimeloyl-ACP esters. E.coli employs a methylation and demethylation strategy to allow elongation of a temporarily disguised malonate moiety to a pimelate moiety by the fatty acid synthetic enzymes. BioH shows a preference for short chain fatty acid esters (acyl chain length of up to 6 carbons) and short chain p-nitrophenyl esters. Also displays a weak thioesterase activity. Can form a complex with CoA, and may be involved in the condensation of CoA and pimelic acid into pimeloyl-CoA, a precursor in biotin biosynthesis.; FUNCTION: Catalyzes the hydrolysis of the methyl ester bond of dimethylbutyryl-S-methyl mercaptopropionate (DMB-S-MMP) to yield dimethylbutyryl mercaptopropionic acid (DMBS-MPA) during the biocatalytic conversion of simvastin acid from monacolin J acid. Can also use acyl carriers such as dimethylbutyryl-S-ethyl mercaptopropionate (DMB-S-EMP) and dimethylbutyryl-S-methyl thioglycolate (DMB-S-MTG) as the thioester substrates. BioH is an esterase that hydrolyzes the methyl ester of pimeloyl-[acp]|, terminating the part of the biotin biosynthesis pathway that is catalyzed by the fatty acid synthesis enzymes...

## Biological Role

Catalyzes CARBOXYLESTERASE-RXN (reaction.ecocyc.CARBOXYLESTERASE-RXN), RXN-11483 (reaction.ecocyc.RXN-11483).

## Enriched Pathways

- `eco00780` Biotin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: The physiological role of BioH is to remove the methyl group introduced by BioC when the pimeloyl moiety is complete. It allows to synthesize pimeloyl-ACP via the fatty acid synthetic pathway through the hydrolysis of the ester bonds of pimeloyl-ACP esters. E.coli employs a methylation and demethylation strategy to allow elongation of a temporarily disguised malonate moiety to a pimelate moiety by the fatty acid synthetic enzymes. BioH shows a preference for short chain fatty acid esters (acyl chain length of up to 6 carbons) and short chain p-nitrophenyl esters. Also displays a weak thioesterase activity. Can form a complex with CoA, and may be involved in the condensation of CoA and pimelic acid into pimeloyl-CoA, a precursor in biotin biosynthesis.; FUNCTION: Catalyzes the hydrolysis of the methyl ester bond of dimethylbutyryl-S-methyl mercaptopropionate (DMB-S-MMP) to yield dimethylbutyryl mercaptopropionic acid (DMBS-MPA) during the biocatalytic conversion of simvastin acid from monacolin J acid. Can also use acyl carriers such as dimethylbutyryl-S-ethyl mercaptopropionate (DMB-S-EMP) and dimethylbutyryl-S-methyl thioglycolate (DMB-S-MTG) as the thioester substrates.

## Pathways

- `eco00780` Biotin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.CARBOXYLESTERASE-RXN|reaction.ecocyc.CARBOXYLESTERASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-11483|reaction.ecocyc.RXN-11483]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3412|gene.b3412]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P13001`
- `KEGG:ecj:JW3375;eco:b3412;ecoc:C3026_18510;`
- `GeneID:947916;`
- `GO:GO:0005737; GO:0009102; GO:0052689; GO:0090499; GO:0106435`
- `EC:3.1.1.85`

## Notes

Pimeloyl-[acyl-carrier protein] methyl ester esterase (EC 3.1.1.85) (Biotin synthesis protein BioH) (Carboxylesterase BioH)
