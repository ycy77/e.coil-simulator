---
entity_id: "protein.P0AFR2"
entity_type: "protein"
name: "dauA"
source_database: "UniProt"
source_id: "P0AFR2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:23278959}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dauA ychM b1206 JW5189"
---

# dauA

`protein.P0AFR2`

## Static

- Type: `protein`
- Source: `UniProt:P0AFR2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:23278959}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Responsible for the aerobic transport of succinate from the periplasm to the cytoplasm at acidic pH (PubMed:23278959). Can transport other C4-dicarboxylic acids such as aspartate and fumarate (PubMed:23278959). May also play a role in the regulation of C4-dicarboxylic acid metabolism at pH 7, via regulation of expression and/or activity of DctA. May act as a co-sensor of DcuS (PubMed:23278959). {ECO:0000269|PubMed:23278959}. DauA is an inner membrane protein that transports C4 dicarboxylates in an aerobic, acidic (pH 5) environment. DauA transports the monoanion and dianion form of succinate and fumarate, and the dicarboxylic amino acid aspartate. At pH 5, DauA is the main succinate transporter and DCTA-MONOMER "DctA", which is active for dicarboxylate transport at pH 7, is not produced . DauA is required for the optimal expression of DctA at pH 7 . In liquid culture (pH 5) with succinate as the sole carbon source a dauA deletion mutant and a dauA dctA double deletion mutant are unable to grow. In liquid culture (pH 7) with succinate as sole carbon source a dctA deletion mutant grows poorly when compared to a dauA deletion mutant and both grow less than the wild type . DauA can be detected during growth with succinate at pH 5 or pH 7...

## Biological Role

Catalyzes succinate:proton symport (reaction.ecocyc.TRANS-RXN-121), aspartate:proton symport (reaction.ecocyc.TRANS-RXN-122A), fumarate:proton symport (reaction.ecocyc.TRANS-RXN0-553). Transports Succinate (molecule.C00042), L-Aspartate (molecule.C00049).

## Annotation

FUNCTION: Responsible for the aerobic transport of succinate from the periplasm to the cytoplasm at acidic pH (PubMed:23278959). Can transport other C4-dicarboxylic acids such as aspartate and fumarate (PubMed:23278959). May also play a role in the regulation of C4-dicarboxylic acid metabolism at pH 7, via regulation of expression and/or activity of DctA. May act as a co-sensor of DcuS (PubMed:23278959). {ECO:0000269|PubMed:23278959}.

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-121|reaction.ecocyc.TRANS-RXN-121]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-122A|reaction.ecocyc.TRANS-RXN-122A]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-553|reaction.ecocyc.TRANS-RXN0-553]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00049|molecule.C00049]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b1206|gene.b1206]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFR2`
- `KEGG:ecj:JW5189;eco:b1206;`
- `GeneID:75203319;945770;`
- `GO:GO:0005886; GO:0008271; GO:0015138; GO:0015141; GO:0015183; GO:0015741; GO:0015810; GO:0022857; GO:0055085; GO:0071422`

## Notes

C4-dicarboxylic acid transporter DauA (Dicarboxylic acid uptake system A)
