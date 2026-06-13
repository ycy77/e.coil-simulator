---
entity_id: "complex.ecocyc.BIOTIN-SYN-CPLX"
entity_type: "complex"
name: "biotin synthase"
source_database: "EcoCyc"
source_id: "BIOTIN-SYN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "BioB"
---

# biotin synthase

`complex.ecocyc.BIOTIN-SYN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:BIOTIN-SYN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P12996|protein.P12996]]

## Enriched Summary

Biotin synthase catalyzes the final reaction of biotin biosynthesis by inserting a sulfur atom between C6 and C9 of dethiobiotin in a S-adenosylmethoinine (SAM)-dependent reaction. For a long time, it was not possible to reconstitute a catalytic reaction in vitro, and uncertainty regarding the reaction mechanism, cofactor requirements, and the source of the sulfur atom remained . However, under optimal conditions with pure substrate and removal of the inhibitory 5'-deoxyadenosine product, burst kinetics and multiple turnovers of the enzyme can be observed . BioB belongs to the family of "radical SAM" enzymes . The enzyme purifies as a homodimer . It contains two distinct iron-sulfur binding sites; one carries an air-stable [2Fe-2S] cluster, and the other an air-sensitive [4Fe-4S] cluster that binds SAM and facilitates its reductive cleavage to generate a 5'-deoxyadenosyl radical (dA·) which activates dethiobiotin . E. coli bioB encodes a Type I ([2Fe-2S]-sacrificial) biotin synthase; Type I enzymes likely evolved in aerobes from ancestral Type II ([4Fe-5S]-sacrificial) synthases . A crystal structure of biotin synthase has been solved at 3.4 Å resolution . Reaction mechanisms involving either the [2Fe-2S] cluster or the cofactor PLP were proposed; however, the crystal structure and the cofactor composition of the enzyme do not support involvement of PLP...

## Biological Role

Catalyzes RXN-25310 (reaction.ecocyc.RXN-25310). Bound by a [2Fe-2S] iron-sulfur cluster (molecule.ecocyc.CPD-6), a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Annotation

Biotin synthase catalyzes the final reaction of biotin biosynthesis by inserting a sulfur atom between C6 and C9 of dethiobiotin in a S-adenosylmethoinine (SAM)-dependent reaction. For a long time, it was not possible to reconstitute a catalytic reaction in vitro, and uncertainty regarding the reaction mechanism, cofactor requirements, and the source of the sulfur atom remained . However, under optimal conditions with pure substrate and removal of the inhibitory 5'-deoxyadenosine product, burst kinetics and multiple turnovers of the enzyme can be observed . BioB belongs to the family of "radical SAM" enzymes . The enzyme purifies as a homodimer . It contains two distinct iron-sulfur binding sites; one carries an air-stable [2Fe-2S] cluster, and the other an air-sensitive [4Fe-4S] cluster that binds SAM and facilitates its reductive cleavage to generate a 5'-deoxyadenosyl radical (dA·) which activates dethiobiotin . E. coli bioB encodes a Type I ([2Fe-2S]-sacrificial) biotin synthase; Type I enzymes likely evolved in aerobes from ancestral Type II ([4Fe-5S]-sacrificial) synthases . A crystal structure of biotin synthase has been solved at 3.4 Å resolution . Reaction mechanisms involving either the [2Fe-2S] cluster or the cofactor PLP were proposed; however, the crystal structure and the cofactor composition of the enzyme do not support involvement of PLP. Finally, genetic experiments using a pdxH mutant unable to produce PLP showed that BioB activity does not depend on PLP in vivo . Recent experiments have suggested that the [2Fe-2S] cluster is the source of the sulfur atom. Consistent with its proposed role as the sulfur donor, degradation of the [2Fe-2S] cluster as well as exchange of sulfur atoms between the [2Fe-2S] and [4Fe-4S] clusters is observed during turnover o

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-25310|reaction.ecocyc.RXN-25310]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.ecocyc.CPD-6|molecule.ecocyc.CPD-6]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P12996|protein.P12996]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:BIOTIN-SYN-CPLX`
- `QSPROTEOME:QS00181745`

## Notes

2*protein.P12996
