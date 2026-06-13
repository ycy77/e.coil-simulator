---
entity_id: "protein.P0A6L9"
entity_type: "protein"
name: "hscB"
source_database: "UniProt"
source_id: "P0A6L9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hscB yfhE b2527 JW2511"
---

# hscB

`protein.P0A6L9`

## Static

- Type: `protein`
- Source: `UniProt:P0A6L9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Co-chaperone involved in the maturation of iron-sulfur cluster-containing proteins. Seems to help targeting proteins to be folded toward HscA. The EG12130-MONOMER together with EG12131-MONOMER comprises a chaperone/cochaperone system similar to DnaK/DnaJ that is involved in iron-sulfur cluster assembly . Models for chaperone-facilitated Fe-S cluster transfer have been proposed. One model involves an exchange of Fe-S cluster ligands in the iron-sulfur cluster scaffold protein G7324-MONOMER IscU upon chaperone binding that facilitates cluster transfer ; another involves chaperone-mediated disordering of IscU that promotes the transfer of the Fe-S cluster to an acceptor protein . A crystal structure of HscB has been solved at 1.8 Å resolution . HscB consists of an N-terminal J-domain that is similar to the J-domain of DnaJ, and a compact three-helix bundle C-terminal domain . A solution structure indicates that the crystal structure is representative of the solution state . HscB is a co-chaperone that stimulates HscA (Hsc66) ATPase activity . HscB physically interacts with HscA and with IscU and aids in targeting IscU to HscA . The J-domain of HscB interacts primarily with full-length ATP-bound HscA . The in vivo turnover rate of the HscA chaperone cycle may be determined by the availability of the IscU-HscB complex...

## Biological Role

Component of [Fe-S] cluster biosynthesis chaperone/co-chaperone system (complex.ecocyc.CPLX0-12620).

## Annotation

FUNCTION: Co-chaperone involved in the maturation of iron-sulfur cluster-containing proteins. Seems to help targeting proteins to be folded toward HscA.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-12620|complex.ecocyc.CPLX0-12620]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2527|gene.b2527]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6L9`
- `KEGG:ecj:JW2511;eco:b2527;ecoc:C3026_14005;`
- `GeneID:75172640;946995;`
- `GO:GO:0001671; GO:0005829; GO:0006457; GO:0044571; GO:0051087; GO:0051259; GO:1990230`

## Notes

Co-chaperone protein HscB (Hsc20)
