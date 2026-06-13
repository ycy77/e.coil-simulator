---
entity_id: "complex.ecocyc.CPLX0-1541"
entity_type: "complex"
name: "5'-methylthioadenosine/S-adenosylhomocysteine nucleosidase"
source_database: "EcoCyc"
source_id: "CPLX0-1541"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 5'-methylthioadenosine/S-adenosylhomocysteine nucleosidase

`complex.ecocyc.CPLX0-1541`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-1541`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AF12|protein.P0AF12]]

## Enriched Summary

The mtn gene encodes 5'-methylthioadenosine/S-adenosylhomocysteine nucleosidase . The enzyme catalyzes glycosidic bond cleavage in S-adenosylhomocysteine (SAH) and 5'-methylthioadenosine (MTA) substrates, with a higher Vmax toward 5'-methylthioadenosine . Although MTA was thought to be the preferred substrate , it was later shown that 5'-methylthioadenosine, S-adenosylhomocysteine and 5'-deoxyadenosine are hydrolyzed with similar catalytic efficiency . The E. coli B enzyme has been characterized in detail . The enzyme is an essential component of the pathway responsible for the recycling SAH, the major byproduct of SAM-mediated methylation reactions (see PWY-6151), while simultaneously producing a precursor of the universal quorum sensing signal, autoinducer-2 (see PWY-6153). Crystal structures of the enzyme bound to adenine (1.9 Å resolution) , formycin A (2.2 Å resolution) , and 5'-methylthiotubercidin (2.0 Å resolution) have been presented, and the implications of the structures with respect to catalysis were discussed . Additional crystal structures of the wild-type and mutant enzymes have been determined, allowing analysis of the conformational motions occuring during the catalytic cycle . Conformational flexibility of the active site appears to be important for substrate specificity of the enzyme...

## Biological Role

Catalyzes ADENOSYLHOMOCYSTEINE-NUCLEOSIDASE-RXN (reaction.ecocyc.ADENOSYLHOMOCYSTEINE-NUCLEOSIDASE-RXN), METHYLTHIOADENOSINE-NUCLEOSIDASE-RXN (reaction.ecocyc.METHYLTHIOADENOSINE-NUCLEOSIDASE-RXN), RXN0-6550 (reaction.ecocyc.RXN0-6550).

## Annotation

The mtn gene encodes 5'-methylthioadenosine/S-adenosylhomocysteine nucleosidase . The enzyme catalyzes glycosidic bond cleavage in S-adenosylhomocysteine (SAH) and 5'-methylthioadenosine (MTA) substrates, with a higher Vmax toward 5'-methylthioadenosine . Although MTA was thought to be the preferred substrate , it was later shown that 5'-methylthioadenosine, S-adenosylhomocysteine and 5'-deoxyadenosine are hydrolyzed with similar catalytic efficiency . The E. coli B enzyme has been characterized in detail . The enzyme is an essential component of the pathway responsible for the recycling SAH, the major byproduct of SAM-mediated methylation reactions (see PWY-6151), while simultaneously producing a precursor of the universal quorum sensing signal, autoinducer-2 (see PWY-6153). Crystal structures of the enzyme bound to adenine (1.9 Å resolution) , formycin A (2.2 Å resolution) , and 5'-methylthiotubercidin (2.0 Å resolution) have been presented, and the implications of the structures with respect to catalysis were discussed . Additional crystal structures of the wild-type and mutant enzymes have been determined, allowing analysis of the conformational motions occuring during the catalytic cycle . Conformational flexibility of the active site appears to be important for substrate specificity of the enzyme . Transition state analogue inhibitors of the enzyme have been designed and tested . Mtn has potential as a drug target , and an SAH riboswitch reporter system has been developed to identify potential inhibitors . Expression of mtn increases at the end of log phase growth and can be increased by salt stress . An mtn mutant is auxotrophic for biotin due to the accumulation of 5'-deoxyadenosine, which inhibits biotin synthase activity . Deletion of mtn decreases AI-2 produc

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.ADENOSYLHOMOCYSTEINE-NUCLEOSIDASE-RXN|reaction.ecocyc.ADENOSYLHOMOCYSTEINE-NUCLEOSIDASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.METHYLTHIOADENOSINE-NUCLEOSIDASE-RXN|reaction.ecocyc.METHYLTHIOADENOSINE-NUCLEOSIDASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6550|reaction.ecocyc.RXN0-6550]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AF12|protein.P0AF12]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-1541`
- `QSPROTEOME:QS00196171`

## Notes

2*protein.P0AF12
