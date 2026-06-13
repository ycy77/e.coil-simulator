---
entity_id: "complex.ecocyc.CPLX0-7802"
entity_type: "complex"
name: "diguanylate cyclase DgcZ"
source_database: "EcoCyc"
source_id: "CPLX0-7802"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# diguanylate cyclase DgcZ

`complex.ecocyc.CPLX0-7802`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7802`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P31129|protein.P31129]]

## Enriched Summary

DgcZ is an EC-2.7.7.65, that regulates motility and biofilm formation; its effect is probably mediated by the second messenger molecule C-DI-GMP (c-di-GMP) . DgcZ activity is allosterically regulated by zinc, which appears to impede the motility of the catalytic GGDEF domains of the dimeric enzyme, thus preventing a productive encounter of the two GTP substrates . A crystal structure of full-length DgcZ has been solved at 3.9 Å resolution . The protein consists of an N-terminal CZB (chemoreceptor zinc binding) domain and a C-terminal GGDEF domain . GTP-based inhibitors of DgcZ activity have been identified . The K4, K170, and K277 residues were found to be acetylated and can be deacetylated by CPLX0-8550 CobB. Deacetylation by CobB increased the in vitro catalytic activity as well as the stability of DgcZ . The DgcZ protein localizes to one of the cell poles in response to carbon starvation and alkaline pH at stationary phase . The physical interaction of DgcZ with the FUM-FE-S FrdB subunit of FUMARATE-REDUCTASE is hypothesized to affect the assembly of flagella . The isolated GGDEF domain of DgcZ was shown to physically interact with the degenerate GGDEF domain of CPLX0-8555 . The PgaABCD machinery, which produces the exopolysaccharide CPD0-1192, depends on DgcZ, and a dgcZ deletion mutant shows reduced surface attachment and reduced CPD0-1192 production...

## Biological Role

Catalyzes RXN0-5359 (reaction.ecocyc.RXN0-5359).

## Annotation

DgcZ is an EC-2.7.7.65, that regulates motility and biofilm formation; its effect is probably mediated by the second messenger molecule C-DI-GMP (c-di-GMP) . DgcZ activity is allosterically regulated by zinc, which appears to impede the motility of the catalytic GGDEF domains of the dimeric enzyme, thus preventing a productive encounter of the two GTP substrates . A crystal structure of full-length DgcZ has been solved at 3.9 Å resolution . The protein consists of an N-terminal CZB (chemoreceptor zinc binding) domain and a C-terminal GGDEF domain . GTP-based inhibitors of DgcZ activity have been identified . The K4, K170, and K277 residues were found to be acetylated and can be deacetylated by CPLX0-8550 CobB. Deacetylation by CobB increased the in vitro catalytic activity as well as the stability of DgcZ . The DgcZ protein localizes to one of the cell poles in response to carbon starvation and alkaline pH at stationary phase . The physical interaction of DgcZ with the FUM-FE-S FrdB subunit of FUMARATE-REDUCTASE is hypothesized to affect the assembly of flagella . The isolated GGDEF domain of DgcZ was shown to physically interact with the degenerate GGDEF domain of CPLX0-8555 . The PgaABCD machinery, which produces the exopolysaccharide CPD0-1192, depends on DgcZ, and a dgcZ deletion mutant shows reduced surface attachment and reduced CPD0-1192 production. dgcZ is required for aminoglycoside-mediated induction of biofilm formation . DgcZ is the major diguanylate cyclase responsible for GlcNAc induction under laboratory conditions . The effect on biofilm formation of overproduction of EG12137-MONOMER is dependent on DgcZ . Overexpression of DgcZ represses swimming behavior, reduces the abundance of flagella and abolishes the appearance of pili-like structures . Expressio

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5359|reaction.ecocyc.RXN0-5359]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P31129|protein.P31129]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7802`
- `QSPROTEOME:QS00183033`

## Notes

2*protein.P31129
