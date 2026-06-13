---
entity_id: "complex.ecocyc.E2O"
entity_type: "complex"
name: "2-oxoglutarate dehydrogenase E2 subunit"
source_database: "EcoCyc"
source_id: "E2O"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 2-oxoglutarate dehydrogenase E2 subunit

`complex.ecocyc.E2O`

## Static

- Type: `complex`
- Source: `EcoCyc:E2O`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0AFG6|protein.P0AFG6]]

## Enriched Summary

E. coli SucB is responsible for the dihydrolipoyltranssuccinylase (dihydrolipoamide succinyltransferase) activity of the 2-oxoglutarate dehydrogenase multienzyme complex (OGDHC) that catalyzes the conversion of 2-oxoglutarate (2-ketoglutarate) to succinyl-CoA and carbon dioxide, with the production of NADH (see PWY-5084). SucB catalyzes the transfer of a succinyl group from the S-succinyldihydrolipoyl moiety to coenzyme A, forming succinyl-CoA. The OGDHC is a member of the 2-oxo acid dehydrogenase family . Members of this family contain multiple copies of three enzymatic components: 2-oxoglutarate decarboxylase (E1), lipoamide acyltransferase (E2) and lipoamide dehydrogenase (E3). In most Gram-positive bacteria and in mitochondria the E1 component is a heterodimer composed of two subunits, while in most (but not all) Gram-negative bacteria it is made up of a single type of subunit. In both cases multiple copies of the E1 component along with multiple copies of the E3 component are assembled around an E2 core of 24 subunits with octahedral symmetry, or 60 subunits with eicosahedral symmetry (depending on which complex and species) . In E. coli the E3 component is shared with the pyruvate dehydrogenase and glycine cleavage multi-enzyme complexes...

## Biological Role

Catalyzes RXN0-1147 (reaction.ecocyc.RXN0-1147). Component of 2-oxoglutarate dehydrogenase complex (complex.ecocyc.2OXOGLUTARATEDEH-CPLX).

## Annotation

E. coli SucB is responsible for the dihydrolipoyltranssuccinylase (dihydrolipoamide succinyltransferase) activity of the 2-oxoglutarate dehydrogenase multienzyme complex (OGDHC) that catalyzes the conversion of 2-oxoglutarate (2-ketoglutarate) to succinyl-CoA and carbon dioxide, with the production of NADH (see PWY-5084). SucB catalyzes the transfer of a succinyl group from the S-succinyldihydrolipoyl moiety to coenzyme A, forming succinyl-CoA. The OGDHC is a member of the 2-oxo acid dehydrogenase family . Members of this family contain multiple copies of three enzymatic components: 2-oxoglutarate decarboxylase (E1), lipoamide acyltransferase (E2) and lipoamide dehydrogenase (E3). In most Gram-positive bacteria and in mitochondria the E1 component is a heterodimer composed of two subunits, while in most (but not all) Gram-negative bacteria it is made up of a single type of subunit. In both cases multiple copies of the E1 component along with multiple copies of the E3 component are assembled around an E2 core of 24 subunits with octahedral symmetry, or 60 subunits with eicosahedral symmetry (depending on which complex and species) . In E. coli the E3 component is shared with the pyruvate dehydrogenase and glycine cleavage multi-enzyme complexes. E1 and E2 differ slightly for the 2-oxoglutarate and pyruvate dehydrogenase complexes, and are designated (o) and (p) to distinguish them. The E. coli OGDHC contains 12 units of the E1(o) component E1O encoded by sucA, 24 units of the E2(o) component E2O encoded by sucB, and 2 units of the E3 component E3-CPLX encoded by lpd. The 24 E2(o) units form the octahedral core of the complex. They contain lipoyllysine and binding sites for dimers of the E1(o) and E3 subunits. Electron cryotomography showed that they are flexibly tethered

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN0-1147|reaction.ecocyc.RXN0-1147]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.2OXOGLUTARATEDEH-CPLX|complex.ecocyc.2OXOGLUTARATEDEH-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AFG6|protein.P0AFG6]] `EcoCyc` `database` - EcoCyc component coefficient=24 | EcoCyc protcplxs.col coefficient=24

## External IDs

- `EcoCyc:E2O`

## Notes

24*protein.P0AFG6
