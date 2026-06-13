---
entity_id: "protein.P77214"
entity_type: "protein"
name: "cusF"
source_database: "UniProt"
source_id: "P77214"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cusF cusX ylcC b0573 JW0562"
---

# cusF

`protein.P77214`

## Static

- Type: `protein`
- Source: `UniProt:P77214`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm.

## Enriched Summary

FUNCTION: Part of a cation efflux system that mediates resistance to copper and silver. Binds one copper per polypeptide (PubMed:11399769, PubMed:24917681). {ECO:0000269|PubMed:11399769, ECO:0000269|PubMed:24917681}. CusF is a periplasmic binding protein involved in the detoxification of copper and silver ions in E. coli as part of the CusCFBA copper/silver efflux system. CusF forms a five-stranded β-barrel and has been crystallized in its apo form as well as with bound Ag(I) or Cu(I) . CusF is a metallochaperone that specifically binds Ag(I) and Cu(I), but not Cu(II) despite earlier evidence regarding binding of Cu(II) . CusF transfers metal directly to CusB for export . CusF is a pink copper-binding protein and binds one copper ion per monomer . The histidine residue at position 58 and the two methionine residues at positions 69 and 71 are essential for copper/silver binding . Cu(I) binding also involves a strong interaction between the metal ion and the aromatic ring of a tryptophan residue at position 44 . The Trp-44 'capping ligand' serves a protective function, preventing access of oxygen to the Cu(I) center . CusF is susceptible to methionine oxidation; the CPLX0-8213 is implicated in maintaining the reduced form . CusF appears in the periplasmic space after induction with CuCl2 . Comment:

## Biological Role

Component of copper/silver export system (complex.ecocyc.CPLX0-1721).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Part of a cation efflux system that mediates resistance to copper and silver. Binds one copper per polypeptide (PubMed:11399769, PubMed:24917681). {ECO:0000269|PubMed:11399769, ECO:0000269|PubMed:24917681}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-1721|complex.ecocyc.CPLX0-1721]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0573|gene.b0573]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77214`
- `KEGG:ecj:JW0562;eco:b0573;ecoc:C3026_02845;`
- `GeneID:945188;`
- `GO:GO:0005507; GO:0006878; GO:0009636; GO:0010043; GO:0010272; GO:0010273; GO:0016530; GO:0016531; GO:0030288; GO:0035434; GO:0042597; GO:0046688; GO:0046914; GO:0060003; GO:1902601`

## Notes

Cation efflux system protein CusF
