---
entity_id: "molecule.ecocyc.Diacylglycerol-Prolipoproteins"
entity_type: "small_molecule"
name: "an (S-diacyl-sn-glyceryl)-L-cysteinyl-[apolipoprotein]"
source_database: "EcoCyc"
source_id: "Diacylglycerol-Prolipoproteins"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/small_molecule
  - source/EcoCyc
aliases:
---

# an (S-diacyl-sn-glyceryl)-L-cysteinyl-[apolipoprotein]

`molecule.ecocyc.Diacylglycerol-Prolipoproteins`

## Static

- Type: `small_molecule`
- Source: `EcoCyc:Diacylglycerol-Prolipoproteins`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

A prolipoprotein contains an N-terminal signal peptide. The protein is synthesized in the cytoplasm and then translocated across the cytoplasmic membrane. The signal peptide possesses positively charged amino acid residues in the N-terminal region and uncharged amino acids in the central hydrophobic region and contains a characteristic consensus sequence called the lipobox in the C-terminal region. The lipobox sequence is Leu-(Ala/Ser)-(Gly/Ala)-Cys, where the first three residues form the C-terminus of the signal peptide. During maturation the signal peptide is removed by cleavage between the (Gly/Ala) and Cys residues, so that the cysteine residue becomes the N-terminal residue. Due to its hydrophobic region, the signal peptide is embedded in the inner membrane, thus attaching the prolipoprotein to the membrane. In Gram negative bacteria, it is facing the perisplasmic side. The first step in the maturation of lipoprotein involves the formation of a thioether linkage between the sulfhydryl group of the cysteine residue and diacylglycerol, while still embedded in the membrane. The two fatty acids connected to the diacylglycerol are also inserted into the membrane, resulting in three membrane anchors (the two fatty acids and the signal peptide)...

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Annotation

A prolipoprotein contains an N-terminal signal peptide. The protein is synthesized in the cytoplasm and then translocated across the cytoplasmic membrane. The signal peptide possesses positively charged amino acid residues in the N-terminal region and uncharged amino acids in the central hydrophobic region and contains a characteristic consensus sequence called the lipobox in the C-terminal region. The lipobox sequence is Leu-(Ala/Ser)-(Gly/Ala)-Cys, where the first three residues form the C-terminus of the signal peptide. During maturation the signal peptide is removed by cleavage between the (Gly/Ala) and Cys residues, so that the cysteine residue becomes the N-terminal residue. Due to its hydrophobic region, the signal peptide is embedded in the inner membrane, thus attaching the prolipoprotein to the membrane. In Gram negative bacteria, it is facing the perisplasmic side. The first step in the maturation of lipoprotein involves the formation of a thioether linkage between the sulfhydryl group of the cysteine residue and diacylglycerol, while still embedded in the membrane. The two fatty acids connected to the diacylglycerol are also inserted into the membrane, resulting in three membrane anchors (the two fatty acids and the signal peptide). In the next step, the signal lipid is cleaves, leaving the protein attached to the membrane by the two fatty acids of the diacylglycerol molecule .

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.RXN-17362|reaction.ecocyc.RXN-17362]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17363|reaction.ecocyc.RXN-17363]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-19774|reaction.ecocyc.RXN-19774]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `EcoCyc:Diacylglycerol-Prolipoproteins`
- `SEED:cpd26960`
- `METANETX:MNXM17259`
