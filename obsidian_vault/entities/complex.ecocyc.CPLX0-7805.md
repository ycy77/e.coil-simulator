---
entity_id: "complex.ecocyc.CPLX0-7805"
entity_type: "complex"
name: "aldehyde dehydrogenase"
source_database: "EcoCyc"
source_id: "CPLX0-7805"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "YagTSR"
  - "PaoABC"
---

# aldehyde dehydrogenase

`complex.ecocyc.CPLX0-7805`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7805`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P77165|protein.P77165]], [[protein.P77324|protein.P77324]], [[protein.P77489|protein.P77489]]

## Enriched Summary

PaoABC is a periplasmic aldehyde oxidoreductase with a possible role in the detoxification of aldehydes. The purified enzyme oxidises a broad spectrum of aldehydes with a preference for aromatic aldehydes such as vanillin and cinnemaldehyde . Purines are not oxidised by PaoABC . PaoABC binds the molybdopterin cytosine dinucleotide (MCD) form of molybdenum cofactor and contains two [2Fe-2S] clusters and one [4Fe-4S] cluster per protein trimer . Purified PaoABC shows no activity with cytochrome c, NAD+ or oxygen as terminal electron acceptor however spinach ferredoxin was able to accept electrons from reduced PaoABC in vitro leading to the suggestion that ferredoxin may be the electron acceptor in vivo . PaoC is the molybdenum cofactor-binding subunit; PaoB contains FAD and a single [4Fe-4S] cluster, and PaoA contains the [2Fe-2S] clusters. Single deletion mutations in each of the paoA, paoB, and paoC genes results in complete impairment of cell growth in the presence of cinnamaldehyde at pH 4.0 but not at pH values of 6-7 . CPLX0-8110 PaoD is the private chaperone for the insertion of the molybdenum cofactor . PaoABC is a periplasmic aldehyde oxidoreductase with a possible role in the detoxification of aldehydes. The purified enzyme oxidises a broad spectrum of aldehydes with a preference for aromatic aldehydes such as vanillin and cinnemaldehyde...

## Biological Role

Catalyzes CARBOXYLATE-REDUCTASE-RXN (reaction.ecocyc.CARBOXYLATE-REDUCTASE-RXN), RXN-24038 (reaction.ecocyc.RXN-24038), RXN-24042 (reaction.ecocyc.RXN-24042). Bound by FAD (molecule.C00016), Cytidylyl molybdenum cofactor (molecule.C21485), a [2Fe-2S] iron-sulfur cluster (molecule.ecocyc.CPD-6), a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Annotation

PaoABC is a periplasmic aldehyde oxidoreductase with a possible role in the detoxification of aldehydes. The purified enzyme oxidises a broad spectrum of aldehydes with a preference for aromatic aldehydes such as vanillin and cinnemaldehyde . Purines are not oxidised by PaoABC . PaoABC binds the molybdopterin cytosine dinucleotide (MCD) form of molybdenum cofactor and contains two [2Fe-2S] clusters and one [4Fe-4S] cluster per protein trimer . Purified PaoABC shows no activity with cytochrome c, NAD+ or oxygen as terminal electron acceptor however spinach ferredoxin was able to accept electrons from reduced PaoABC in vitro leading to the suggestion that ferredoxin may be the electron acceptor in vivo . PaoC is the molybdenum cofactor-binding subunit; PaoB contains FAD and a single [4Fe-4S] cluster, and PaoA contains the [2Fe-2S] clusters. Single deletion mutations in each of the paoA, paoB, and paoC genes results in complete impairment of cell growth in the presence of cinnamaldehyde at pH 4.0 but not at pH values of 6-7 . CPLX0-8110 PaoD is the private chaperone for the insertion of the molybdenum cofactor .

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.CARBOXYLATE-REDUCTASE-RXN|reaction.ecocyc.CARBOXYLATE-REDUCTASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-24038|reaction.ecocyc.RXN-24038]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-24042|reaction.ecocyc.RXN-24042]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (7)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C21485|molecule.C21485]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CPD-6|molecule.ecocyc.CPD-6]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P77165|protein.P77165]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P77324|protein.P77324]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P77489|protein.P77489]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:CPLX0-7805`
- `PDB:5G5H`
- `PDB:5G5G`
- `PDB:5G5G`
- `QSPROTEOME:QS00187957`

## Notes

1*protein.P77165|1*protein.P77324|1*protein.P77489
