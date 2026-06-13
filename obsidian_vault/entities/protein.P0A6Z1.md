---
entity_id: "protein.P0A6Z1"
entity_type: "protein"
name: "hscA"
source_database: "UniProt"
source_id: "P0A6Z1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hscA hsc b2526 JW2510"
---

# hscA

`protein.P0A6Z1`

## Static

- Type: `protein`
- Source: `UniProt:P0A6Z1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Chaperone involved in the maturation of iron-sulfur cluster-containing proteins. Has a low intrinsic ATPase activity which is markedly stimulated by HscB. Involved in the maturation of IscU. HscA together with HscB comprises a chaperone/cochaperone system similar to DnaK/DnaJ . HscA is required for the assembly of iron-sulfur clusters . Models for chaperone-facilitated Fe-S cluster transfer have been proposed. One model involves an exchange of Fe-S cluster ligands in the iron-sulfur cluster scaffold protein G7324-MONOMER IscU upon chaperone binding that facilitates cluster transfer ; another involves chaperone-mediated disordering of IscU that promotes the transfer of the Fe-S cluster to an acceptor protein . HscA consists of two domains, a nucleotide-binding domain (NBD) that binds and hydrolyzes ATP and a substrate-binding domain that binds IscU . The inter-domain linker peptide is able to stimulate the rate of ATP hydrolysis of the isolated NBD . Under steady-state conditions, ATP hydrolysis rather than ADP/ATP nucleotide exchange is the rate-limiting step in the HscA reaction cycle ; the dissociation rates for ATP and ADP are comparatively fast . IscU is a substrate for HscA ; in the presence of HscB, IscU stimulates the ATPase activity of HscA up to 480-fold...

## Biological Role

Component of [Fe-S] cluster biosynthesis chaperone/co-chaperone system (complex.ecocyc.CPLX0-12620).

## Annotation

FUNCTION: Chaperone involved in the maturation of iron-sulfur cluster-containing proteins. Has a low intrinsic ATPase activity which is markedly stimulated by HscB. Involved in the maturation of IscU.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-12620|complex.ecocyc.CPLX0-12620]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2526|gene.b2526]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6Z1`
- `KEGG:ecj:JW2510;eco:b2526;ecoc:C3026_14000;`
- `GeneID:93774610;944885;`
- `GO:GO:0005524; GO:0005829; GO:0016226; GO:0016887; GO:0031072; GO:0042026; GO:0043531; GO:0044183; GO:0051082; GO:0070417; GO:0140662; GO:1990230`

## Notes

Chaperone protein HscA (Hsc66)
