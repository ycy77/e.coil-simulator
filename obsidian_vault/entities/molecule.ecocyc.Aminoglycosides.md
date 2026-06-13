---
entity_id: "molecule.ecocyc.Aminoglycosides"
entity_type: "small_molecule"
name: "an aminoglycoside"
source_database: "EcoCyc"
source_id: "Aminoglycosides"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/small_molecule
  - source/EcoCyc
aliases:
  - "a aminoglycoside"
---

# an aminoglycoside

`molecule.ecocyc.Aminoglycosides`

## Static

- Type: `small_molecule`
- Source: `EcoCyc:Aminoglycosides`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

An aminoglycoside is a molecule composed of a sugar group and an amino group. Several aminoglycoside function as antibiotics that are used to treat certain bacterial infections. Anthracyclines are another group of aminoglycosides, which are used in chemotherapy. An aminoglycoside is a molecule composed of a sugar group and an amino group. Several aminoglycoside function as antibiotics that are used to treat certain bacterial infections. Anthracyclines are another group of aminoglycosides, which are used in chemotherapy.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 2 reaction(s).

## Annotation

An aminoglycoside is a molecule composed of a sugar group and an amino group. Several aminoglycoside function as antibiotics that are used to treat certain bacterial infections. Anthracyclines are another group of aminoglycosides, which are used in chemotherapy.

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-1551|reaction.ecocyc.TRANS-RXN-1551]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-1552|reaction.ecocyc.TRANS-RXN-1552]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-1551|reaction.ecocyc.TRANS-RXN-1551]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-1552|reaction.ecocyc.TRANS-RXN-1552]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[complex.ecocyc.CPLX0-3932|complex.ecocyc.CPLX0-3932]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `EcoCyc:Aminoglycosides`
- `CHEBI:47779`
