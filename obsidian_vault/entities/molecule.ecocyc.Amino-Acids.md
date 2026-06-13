---
entity_id: "molecule.ecocyc.Amino-Acids"
entity_type: "small_molecule"
name: "an amino acid"
source_database: "EcoCyc"
source_id: "Amino-Acids"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/small_molecule
  - source/EcoCyc
aliases:
---

# an amino acid

`molecule.ecocyc.Amino-Acids`

## Static

- Type: `small_molecule`
- Source: `EcoCyc:Amino-Acids`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

This class contains all of the amino acids, defined as any molecule that contains both amine and carboxyl functional groups. The class includes both α amino acids, in which both functional groups are attached to the same carbon atom, and non-α amino acids, in which the groups are attached to different carbon atoms. This class contains all of the amino acids, defined as any molecule that contains both amine and carboxyl functional groups. The class includes both α amino acids, in which both functional groups are attached to the same carbon atom, and non-α amino acids, in which the groups are attached to different carbon atoms.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 2 reaction(s).

## Annotation

This class contains all of the amino acids, defined as any molecule that contains both amine and carboxyl functional groups. The class includes both α amino acids, in which both functional groups are attached to the same carbon atom, and non-α amino acids, in which the groups are attached to different carbon atoms.

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-265|reaction.ecocyc.TRANS-RXN0-265]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-612|reaction.ecocyc.TRANS-RXN0-612]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.GAMMA-GLUTAMYLTRANSFERASE-RXN|reaction.ecocyc.GAMMA-GLUTAMYLTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-265|reaction.ecocyc.TRANS-RXN0-265]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-612|reaction.ecocyc.TRANS-RXN0-612]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `EcoCyc:Amino-Acids`
- `REACTOME-CPD:2103117`
- `SEED:cpd11612`
- `METANETX:MNXM578`
- `LIGAND-CPD:C00045`
