---
entity_id: "protein.P30748"
entity_type: "protein"
name: "moaD"
source_database: "UniProt"
source_id: "P30748"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "moaD chlA4 chlM b0784 JW0767"
---

# moaD

`protein.P30748`

## Static

- Type: `protein`
- Source: `UniProt:P30748`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in sulfur transfer in the conversion of molybdopterin precursor Z to molybdopterin. {ECO:0000269|PubMed:17223713}. Initially, EG11598-MONOMER (MoeB) was presumed to catalyze transfer of sulfur atoms to CPLX0-2502 , however other evidence indicates that MoeB activates MoaD by adenylylation of MoaD's C-terminus. MoaD appears to further enhance MoeB's activation of G7325-MONOMER . Surface plasmon resonance studies suggested that IscS specifically binds to the putative in vivo MoeB-MoaD complex . It has since been determined that the carboxy-adenylated MoaD is sulfurated by the IscS via TusA or YnjE sulfurtransferases . Purified recombinant MoeB was shown to be a homodimer in solution . It was also shown to form a MoeB-MoaD heterotetrameric complex. Crystal structures of the apo, ATP-bound, and MoaD-adenylate forms of the MoeB-MoaD complex have been determined at 1.7, 2.9 and 2.1 Å resolution, respectively . The interaction between these proteins was also demonstrated in solution . MoaD structurally resembles the ubiquitin and ThiS proteins . MoaD contains a ubiquitin-like fold and a highly conserved Gly-Gly motif that upon activation forms the thiocarboxylate group. In addition to forming the molybdopterin synthase complex with MoaE, MoaD also forms a similar complex with MoeB to regenerate its sulfur after transfer to molybdoptrin...

## Biological Role

Component of molybdopterin synthase adenylyltransferase/sulfur transferase (complex.ecocyc.CPLX0-12611), molybdopterin synthase (complex.ecocyc.CPLX0-2502).

## Enriched Pathways

- `eco04122` Sulfur relay system (KEGG)

## Annotation

FUNCTION: Involved in sulfur transfer in the conversion of molybdopterin precursor Z to molybdopterin. {ECO:0000269|PubMed:17223713}.

## Pathways

- `eco04122` Sulfur relay system (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-12611|complex.ecocyc.CPLX0-12611]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-2502|complex.ecocyc.CPLX0-2502]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0784|gene.b0784]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P30748`
- `KEGG:ecj:JW0767;eco:b0784;ecoc:C3026_04970;`
- `GeneID:945398;`
- `GO:GO:0000166; GO:0005829; GO:0006777; GO:1990133; GO:1990140`

## Notes

Molybdopterin synthase sulfur carrier subunit (MPT synthase subunit 1) (Molybdenum cofactor biosynthesis protein D) (Molybdopterin-converting factor small subunit) (Molybdopterin-converting factor subunit 1) (Sulfur carrier protein MoaD)
