---
entity_id: "molecule.ecocyc.PQQ"
entity_type: "small_molecule"
name: "pyrroloquinoline quinone"
source_database: "EcoCyc"
source_id: "PQQ"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/small_molecule
  - source/EcoCyc
aliases:
  - "coenzyme PQQ"
  - "4,5-dihydro-4,5-dioxo-1H-pyrrolo[2,3-5,6]quinoline-2,7,9-tricarboxylic acid"
  - "2,7,9-tricarboxy-1H-pyrrolo(2,3-f)quinoline-4,5-dione"
  - "2,4,6-tricarboxylic-pyrrolo[2,3-5,6]quinoline 8,9-quinone"
  - "4,5-dioxo-3α,4,5,6,7,8,9,9β-octahydro-1H pyrrolo[2,3-f]quinoline-2,7,9-tricarboxylate"
  - "4,5-dioxo-4,5-dihydro-1H-pyrrolo[2,3-f]quinoline-2,7,9-tricarboxylate"
  - "PQQ"
  - "methoxatin"
  - "2,7,9-tricarboxy-1H-pyrrolo[2,3-f]quinoline-4,5-dione"
---

# pyrroloquinoline quinone

`molecule.ecocyc.PQQ`

## Static

- Type: `small_molecule`
- Source: `EcoCyc:PQQ`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

Pyrroloquinoline quinone (PQQ) is water-soluble, redox-cycling orthoquinone that was initially isolated from cultures of methylotropic bacteria. It has been found to be a cofactor of several bacterial enzymes, and is present in many animal tissues . Several researchers suggested that PQQ should be considered a member of the vitamin B group although this claim has been contested . Pyrroloquinoline quinone (PQQ) is water-soluble, redox-cycling orthoquinone that was initially isolated from cultures of methylotropic bacteria. It has been found to be a cofactor of several bacterial enzymes, and is present in many animal tissues . Several researchers suggested that PQQ should be considered a member of the vitamin B group although this claim has been contested .

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s). Binds gcd (protein.P15877), yliI (protein.P75804).

## Annotation

Pyrroloquinoline quinone (PQQ) is water-soluble, redox-cycling orthoquinone that was initially isolated from cultures of methylotropic bacteria. It has been found to be a cofactor of several bacterial enzymes, and is present in many animal tissues . Several researchers suggested that PQQ should be considered a member of the vitamin B group although this claim has been contested .

## Outgoing Edges (4)

- `binds` --> [[protein.P15877|protein.P15877]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[protein.P75804|protein.P75804]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-629|reaction.ecocyc.TRANS-RXN0-629]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-629|reaction.ecocyc.TRANS-RXN0-629]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[complex.ecocyc.CPLX0-9372|complex.ecocyc.CPLX0-9372]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `EcoCyc:PQQ`
- `ZINC:ZINC000001532545`
- `SEED:cpd00097`
- `METANETX:MNXM601`
- `HMDB:HMDB13636`
- `PUBCHEM:23615439`
- `CHEBI:58442`
- `LIGAND-CPD:C00113`
- `CAS:72909-34-3`
- `DRUGBANK:DB03205`
- `CHEMSPIDER:19951489`

## Notes

(C 14)
