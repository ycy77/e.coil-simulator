---
entity_id: "protein.P0AE01"
entity_type: "protein"
name: "trmJ"
source_database: "UniProt"
source_id: "P0AE01"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "trmJ yfhQ b2532 JW2516"
---

# trmJ

`protein.P0AE01`

## Static

- Type: `protein`
- Source: `UniProt:P0AE01`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Catalyzes the formation of 2'O-methylated cytidine (Cm32) or 2'O-methylated uridine (Um32) at position 32 in tRNA (PubMed:16848900, PubMed:24951554, PubMed:26202969). Can also methylate adenosine or guanosine, even though these nucleosides are rare or absent at position 32 in the anticodon loop of tRNA (PubMed:24951554). {ECO:0000269|PubMed:16848900, ECO:0000269|PubMed:24951554, ECO:0000269|PubMed:26202969}. TrmJ is the tRNA:Cm32/Um32 methyltransferase which introduces methyl groups at the 2'-O position of C32 and U32 of several tRNAs in vitro. The tRNAs 2'-O-methylated at the C/U32 position in vivo are glnW-tRNA and glnX-tRNA (at the U32 position), and metZ-tRNA, metY-tRNA, serT-tRNA and trpT-tRNA (at the C32 position) . TrmJ belongs to the SPOUT superfamily of methyltransferases . Sequence analysis suggests that the active sites of TrmH and TrmJ are conserved, and the enzymes may thus use a similar reaction mechanism . TrmJ does not show specificity for the nucleotide at the 32 position and can also methylate tRNAPro(GGG) in vitro . Crystal structures of the N-terminal SPOUT domain of TrmJ as well as the full-length enzyme in complex with SAH have been solved . The enzyme forms an unusual asymmetric dimer in which the N- and C-terminal domains associate separately. SAH is bound to the trefoil knot within the SPOUT domain...

## Biological Role

Component of tRNA Cm32/Um32 methyltransferase (complex.ecocyc.CPLX0-7420).

## Annotation

FUNCTION: Catalyzes the formation of 2'O-methylated cytidine (Cm32) or 2'O-methylated uridine (Um32) at position 32 in tRNA (PubMed:16848900, PubMed:24951554, PubMed:26202969). Can also methylate adenosine or guanosine, even though these nucleosides are rare or absent at position 32 in the anticodon loop of tRNA (PubMed:24951554). {ECO:0000269|PubMed:16848900, ECO:0000269|PubMed:24951554, ECO:0000269|PubMed:26202969}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7420|complex.ecocyc.CPLX0-7420]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2532|gene.b2532]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AE01`
- `KEGG:ecj:JW2516;eco:b2532;ecoc:C3026_14030;`
- `GeneID:86860658;948610;`
- `GO:GO:0002128; GO:0003723; GO:0005829; GO:0042803; GO:0106339; GO:0160206`
- `EC:2.1.1.200`

## Notes

tRNA (cytidine/uridine-2'-O-)-methyltransferase TrmJ (EC 2.1.1.200) (TrMet(Xm32)) (tRNA (cytidine(32)/uridine(32)-2'-O)-methyltransferase) (tRNA Cm32/Um32 methyltransferase)
