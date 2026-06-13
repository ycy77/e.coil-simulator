---
entity_id: "protein.P0A847"
entity_type: "protein"
name: "tgt"
source_database: "UniProt"
source_id: "P0A847"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tgt b0406 JW0396"
---

# tgt

`protein.P0A847`

## Static

- Type: `protein`
- Source: `UniProt:P0A847`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the base-exchange of a guanine (G) residue with the queuine precursor 7-aminomethyl-7-deazaguanine (PreQ1) at position 34 (anticodon wobble position) in tRNAs with GU(N) anticodons (tRNA-Asp, -Asn, -His and -Tyr). Catalysis occurs through a double-displacement mechanism. The nucleophile active site attacks the C1' of nucleotide 34 to detach the guanine base from the RNA, forming a covalent enzyme-RNA intermediate. The proton acceptor active site deprotonates the incoming PreQ1, allowing a nucleophilic attack on the C1' of the ribose to form the product. After dissociation, two additional enzymatic reactions on the tRNA convert PreQ1 to queuine (Q), resulting in the hypermodified nucleoside queuosine (7-(((4,5-cis-dihydroxy-2-cyclopenten-1-yl)amino)methyl)-7-deazaguanosine). {ECO:0000255|HAMAP-Rule:MF_00168, ECO:0000269|PubMed:11714265, ECO:0000269|PubMed:12909636}.

## Biological Role

Catalyzes tRNA-guanosine34:7-aminomethyl-7-carbaguanine tRNA-D-ribosyltransferase (reaction.R10209). Component of tRNA-guanine transglycosylase (complex.ecocyc.CPLX0-1101).

## Annotation

FUNCTION: Catalyzes the base-exchange of a guanine (G) residue with the queuine precursor 7-aminomethyl-7-deazaguanine (PreQ1) at position 34 (anticodon wobble position) in tRNAs with GU(N) anticodons (tRNA-Asp, -Asn, -His and -Tyr). Catalysis occurs through a double-displacement mechanism. The nucleophile active site attacks the C1' of nucleotide 34 to detach the guanine base from the RNA, forming a covalent enzyme-RNA intermediate. The proton acceptor active site deprotonates the incoming PreQ1, allowing a nucleophilic attack on the C1' of the ribose to form the product. After dissociation, two additional enzymatic reactions on the tRNA convert PreQ1 to queuine (Q), resulting in the hypermodified nucleoside queuosine (7-(((4,5-cis-dihydroxy-2-cyclopenten-1-yl)amino)methyl)-7-deazaguanosine). {ECO:0000255|HAMAP-Rule:MF_00168, ECO:0000269|PubMed:11714265, ECO:0000269|PubMed:12909636}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R10209|reaction.R10209]] `KEGG` `database` - via EC:2.4.2.29
- `is_component_of` --> [[complex.ecocyc.CPLX0-1101|complex.ecocyc.CPLX0-1101]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b0406|gene.b0406]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A847`
- `KEGG:ecj:JW0396;eco:b0406;ecoc:C3026_01975;`
- `GeneID:93777054;949130;`
- `GO:GO:0002099; GO:0005737; GO:0005829; GO:0008270; GO:0008479; GO:0008616`
- `EC:2.4.2.29`

## Notes

Queuine tRNA-ribosyltransferase (EC 2.4.2.29) (Guanine insertion enzyme) (tRNA-guanine transglycosylase)
