---
entity_id: "protein.P04982"
entity_type: "protein"
name: "rbsD"
source_database: "UniProt"
source_id: "P04982"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rbsD b3748 JW5857"
---

# rbsD

`protein.P04982`

## Static

- Type: `protein`
- Source: `UniProt:P04982`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Catalyzes the interconversion of beta-pyran and beta-furan forms of D-ribose. It also catalyzes the conversion between beta-allofuranose and beta-allopyranose. {ECO:0000269|PubMed:15060078}. RbsD is a ribose pyranase; it binds specifically to the β-furan and β-pyran forms of ribose and increases the exchange rate between the two forms . A preliminary crystallographic analysis of RbsD was reported, but no structure coordinates were deposited with PDB . Based on analytical centrifugation analysis, RbsD was initially reported to be an octamer in solution ; analysis of the crystal structure showed it to be a decamer, similar to the Bacillus subtilis homolog , while gel permeation chromatography indicated that the protein was a heptamer . Under urea-induced denaturation conditions, the homodecamer undergoes stepwise disassembly and non-stepwise reassembly . The Lys2 residue appears to be involved in stabilization of the oligomeric state . The RbsD protein is required for efficient utilization of ribose when ribose is transported into the cell via a mutated form of PtsG, the glucose transporter. A mutation in rbsD does not abolish ribose transport . An rbsD point mutant that abolishes pyranase activity is impaired in the utilization of D-ribose as a source of carbon and energy . Overproduction of RbsD inhibits growth on D-ribose due to accumulation of methylglyoxal...

## Biological Role

Component of D-ribose pyranase (complex.ecocyc.CPLX0-7646).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Catalyzes the interconversion of beta-pyran and beta-furan forms of D-ribose. It also catalyzes the conversion between beta-allofuranose and beta-allopyranose. {ECO:0000269|PubMed:15060078}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7646|complex.ecocyc.CPLX0-7646]] `EcoCyc` `database` - EcoCyc component coefficient=10 | EcoCyc protcplxs.col coefficient=10

## Incoming Edges (1)

- `encodes` <-- [[gene.b3748|gene.b3748]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P04982`
- `KEGG:ecj:JW5857;eco:b3748;ecoc:C3026_20305;`
- `GeneID:75173982;948267;`
- `GO:GO:0005829; GO:0016866; GO:0016872; GO:0019303; GO:0042802; GO:0048029; GO:0062193`
- `EC:5.4.99.62`

## Notes

D-ribose pyranase (EC 5.4.99.62)
