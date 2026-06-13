---
entity_id: "protein.P16431"
entity_type: "protein"
name: "hycE"
source_database: "UniProt"
source_id: "P16431"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hycE hevE b2721 JW2691"
---

# hycE

`protein.P16431`

## Static

- Type: `protein`
- Source: `UniProt:P16431`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Formate hydrogenlyase subunit 5 (FHL subunit 5) (Hydrogenase-3 component E) The hycBCDEFG genes in E. coli K-12 encode the hydrogenase component (hydrogenase 3) of the formate hydrogenlyase complex. HycE is the large subunit of hydrogenase 3 ; it contains the nickel-iron active site where protons are reduced to H2 (see ). Maturation of HycE requires incorporation of nickel followed by processing after the Arg537 residue by the HycI maturation endopeptidase . Maturation has been reconstituted in vitro and requires HypB, HypC, HypD, HypE, HypF, HycI and nickel, as it does in vivo . HypC interacts directly with pre-HycE and facilitates metal incorporation ; mutational studies of conserved cysteine residues have led to a model for nickel incorporation . After the incorporation of nickel, pre-HycE must dissociate from HypC to become a substrate for the HycI maturation endopeptidase . HycE variants with increased hydrogen-producing activity have been engineered .

## Biological Role

Component of formate hydrogenlyase complex (complex.ecocyc.FHLMULTI-CPLX), hydrogenase 3 (complex.ecocyc.HYDROG3-CPLX).

## Annotation

Formate hydrogenlyase subunit 5 (FHL subunit 5) (Hydrogenase-3 component E)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.FHLMULTI-CPLX|complex.ecocyc.FHLMULTI-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.HYDROG3-CPLX|complex.ecocyc.HYDROG3-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2721|gene.b2721]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P16431`
- `KEGG:ecj:JW2691;eco:b2721;ecoc:C3026_14970;`
- `GeneID:947396;`
- `GO:GO:0006007; GO:0008137; GO:0009061; GO:0009326; GO:0015944; GO:0016151; GO:0016651; GO:0019645; GO:0048038; GO:0051287; GO:0051539`

## Notes

Formate hydrogenlyase subunit 5 (FHL subunit 5) (Hydrogenase-3 component E)
