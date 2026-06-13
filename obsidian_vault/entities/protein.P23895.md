---
entity_id: "protein.P23895"
entity_type: "protein"
name: "emrE"
source_database: "UniProt"
source_id: "P23895"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15044024, ECO:0000269|PubMed:9688273}; Multi-pass membrane protein {ECO:0000269|PubMed:15044024, ECO:0000269|PubMed:17005200, ECO:0000269|PubMed:9688273}. Note=Forms antiparallel homodimers (PubMed:17005200, PubMed:18024586, PubMed:20508091, PubMed:20551331, PubMed:22178925, PubMed:23920359). The topology could be controlled by a single positively charged residue placed in different locations throughout the protein, including the very C terminus (PubMed:20508091). {ECO:0000269|PubMed:17005200, ECO:0000269|PubMed:18024586, ECO:0000269|PubMed:20508091, ECO:0000269|PubMed:20551331, ECO:0000269|PubMed:22178925, ECO:0000269|PubMed:23920359}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "emrE eb mvrC b0543 JW0531"
---

# emrE

`protein.P23895`

## Static

- Type: `protein`
- Source: `UniProt:P23895`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15044024, ECO:0000269|PubMed:9688273}; Multi-pass membrane protein {ECO:0000269|PubMed:15044024, ECO:0000269|PubMed:17005200, ECO:0000269|PubMed:9688273}. Note=Forms antiparallel homodimers (PubMed:17005200, PubMed:18024586, PubMed:20508091, PubMed:20551331, PubMed:22178925, PubMed:23920359). The topology could be controlled by a single positively charged residue placed in different locations throughout the protein, including the very C terminus (PubMed:20508091). {ECO:0000269|PubMed:17005200, ECO:0000269|PubMed:18024586, ECO:0000269|PubMed:20508091, ECO:0000269|PubMed:20551331, ECO:0000269|PubMed:22178925, ECO:0000269|PubMed:23920359}.

## Enriched Summary

FUNCTION: Multidrug efflux protein that confers resistance to a wide range of toxic compounds, including ethidium, methyl viologen, acriflavine, tetraphenylphosphonium (TPP(+)), benzalkonium, propidium, dequalinium and the aminoglycoside antibiotics streptomycin and tobramycin (PubMed:10681497, PubMed:11574548, PubMed:15371426, PubMed:18024586, PubMed:18295794, PubMed:23042996, PubMed:24448799, PubMed:7896833, PubMed:9050242). Can also transport the osmoprotectants betaine and choline (PubMed:22942246). The drug efflux is coupled to an influx of protons (PubMed:15371426, PubMed:29114048, PubMed:7896833). Can couple antiport of a drug to either one or two protons, performing both electrogenic and electroneutral transport of a single substrate (PubMed:29114048). Simultaneously binds and cotransports proton and drug (PubMed:29114048, PubMed:30287687). {ECO:0000269|PubMed:10681497, ECO:0000269|PubMed:11574548, ECO:0000269|PubMed:15371426, ECO:0000269|PubMed:18024586, ECO:0000269|PubMed:18295794, ECO:0000269|PubMed:22942246, ECO:0000269|PubMed:23042996, ECO:0000269|PubMed:24448799, ECO:0000269|PubMed:29114048, ECO:0000269|PubMed:30287687, ECO:0000269|PubMed:7896833, ECO:0000269|PubMed:9050242}.

## Biological Role

Component of multidrug efflux pump EmrE / betaine:H+ antiporter (complex.ecocyc.CPLX0-7963).

## Annotation

FUNCTION: Multidrug efflux protein that confers resistance to a wide range of toxic compounds, including ethidium, methyl viologen, acriflavine, tetraphenylphosphonium (TPP(+)), benzalkonium, propidium, dequalinium and the aminoglycoside antibiotics streptomycin and tobramycin (PubMed:10681497, PubMed:11574548, PubMed:15371426, PubMed:18024586, PubMed:18295794, PubMed:23042996, PubMed:24448799, PubMed:7896833, PubMed:9050242). Can also transport the osmoprotectants betaine and choline (PubMed:22942246). The drug efflux is coupled to an influx of protons (PubMed:15371426, PubMed:29114048, PubMed:7896833). Can couple antiport of a drug to either one or two protons, performing both electrogenic and electroneutral transport of a single substrate (PubMed:29114048). Simultaneously binds and cotransports proton and drug (PubMed:29114048, PubMed:30287687). {ECO:0000269|PubMed:10681497, ECO:0000269|PubMed:11574548, ECO:0000269|PubMed:15371426, ECO:0000269|PubMed:18024586, ECO:0000269|PubMed:18295794, ECO:0000269|PubMed:22942246, ECO:0000269|PubMed:23042996, ECO:0000269|PubMed:24448799, ECO:0000269|PubMed:29114048, ECO:0000269|PubMed:30287687, ECO:0000269|PubMed:7896833, ECO:0000269|PubMed:9050242}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7963|complex.ecocyc.CPLX0-7963]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0543|gene.b0543]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P23895`
- `KEGG:ecj:JW0531;eco:b0543;ecoc:C3026_02670;`
- `GeneID:948442;`
- `GO:GO:0005886; GO:0006805; GO:0006970; GO:0006974; GO:0009410; GO:0015199; GO:0015220; GO:0015297; GO:0015871; GO:0016020; GO:0022857; GO:0031460; GO:0042802; GO:0042908; GO:0042910; GO:0055085; GO:0071466; GO:1990207; GO:1990961`

## Notes

Multidrug transporter EmrE (Efflux-multidrug resistance protein EmrE) (Ethidium resistance protein) (Methyl viologen resistance protein C)
