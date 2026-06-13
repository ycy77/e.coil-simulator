---
entity_id: "complex.ecocyc.CPLX-170"
entity_type: "complex"
name: "galactosamine-specific PTS enzyme II"
source_database: "EcoCyc"
source_id: "CPLX-170"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "EII<sup>Gam</sup>"
  - "Enzyme II<sup>Gam</sup>"
  - "EII<suP>GalN</sup>"
  - "Enzyme II<suP>GalN</sup>"
---

# galactosamine-specific PTS enzyme II

`complex.ecocyc.CPLX-170`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX-170`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P42909|protein.P42909]], [[protein.P42910|protein.P42910]], [[protein.P42911|protein.P42911]]

## Enriched Summary

E. coli contains a cluster of genes (agaZVWEFASYBCDI) responsible for the uptake and metabolism of D-galactosamine (GalN or Gam) and N-acetyl-D-galactosamine (GalNAc or Aga). However, in strain K-12 there is a deletion of the region from agaW' to 'agaA making this organism unable to utilize GalN and GalNAc as sole carbon sources . AgaBCD, the cryptic GalN PTS permease, belongs to the functional superfamily of the phosphoenolpyruvate (PEP)-dependent, sugar transporting phosphotransferase system (PTSsugar). The PTSsugar transports and simultaneously phosphorylates its substrates in a process called group translocation (reviewed in ). When all of its components are present, AgaBCDF takes up exogenous GalN, releasing the phosphate ester into the cell cytoplasm in preparation for metabolism . AgaB is Enzyme IIBGam. AgaC is Enzyme IICGam. AgaD is an Enzyme IIDGam. agaF encoding Enzyme IIAAga/Gam has been deleted. All of these proteins are homologous to the mannose Enzyme II complex proteins (the splinter group enzymes) . E. coli K-12 is Gam- Aga-. Providing agaF (which encodes a PTS Enzyme IIA domain) from E. coli C on a plasmid results in a Gam+ Aga- phenotype...

## Annotation

E. coli contains a cluster of genes (agaZVWEFASYBCDI) responsible for the uptake and metabolism of D-galactosamine (GalN or Gam) and N-acetyl-D-galactosamine (GalNAc or Aga). However, in strain K-12 there is a deletion of the region from agaW' to 'agaA making this organism unable to utilize GalN and GalNAc as sole carbon sources . AgaBCD, the cryptic GalN PTS permease, belongs to the functional superfamily of the phosphoenolpyruvate (PEP)-dependent, sugar transporting phosphotransferase system (PTSsugar). The PTSsugar transports and simultaneously phosphorylates its substrates in a process called group translocation (reviewed in ). When all of its components are present, AgaBCDF takes up exogenous GalN, releasing the phosphate ester into the cell cytoplasm in preparation for metabolism . AgaB is Enzyme IIBGam. AgaC is Enzyme IICGam. AgaD is an Enzyme IIDGam. agaF encoding Enzyme IIAAga/Gam has been deleted. All of these proteins are homologous to the mannose Enzyme II complex proteins (the splinter group enzymes) . E. coli K-12 is Gam- Aga-. Providing agaF (which encodes a PTS Enzyme IIA domain) from E. coli C on a plasmid results in a Gam+ Aga- phenotype . The aga gene cluster (agaZVWASYBCDI) also encodes other enzymes for the metabolism of GalNAc and GalN: GalNAc-6-phosphate deacetylase (EG12766 "AgaA"); a putative isomerase (G7634 "AgaS"); a tagatose-bisphosphate aldolase (CPLX0-240 "KbaYZ" formerly AgaYZ) and a GalN-6-phosphate deaminase (G7636 "AgaI"). The truncated agaA gene in E. coli K-12 is inactive. G7630 "agaR" encodes a transcriptional repressor of the aga gene cluster .

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P42909|protein.P42909]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P42910|protein.P42910]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P42911|protein.P42911]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:CPLX-170`
- `QSPROTEOME:QS00049478`

## Notes

1*protein.P42909|1*protein.P42910|1*protein.P42911
