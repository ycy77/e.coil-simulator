---
entity_id: "protein.P39325"
entity_type: "protein"
name: "ytfQ"
source_database: "UniProt"
source_id: "P39325"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:19744923}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ytfQ b4227 JW4186"
---

# ytfQ

`protein.P39325`

## Static

- Type: `protein`
- Source: `UniProt:P39325`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:19744923}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex YtfQRT-YjfF involved in galactofuranose transport (Probable). Binds to both alpha- and beta-galactofuranose (PubMed:19744923). {ECO:0000269|PubMed:19744923, ECO:0000305|PubMed:19744923}. YtfQ is the periplasmic binding component of a galactofuranose ABC transporter. Purified YtfQ binds galactose with a Kd of 1.7μM and arabinose with a Kd of 1.3μM; YtfQ exhibits selective binding of galactofuranose over galactopyranose; the inferred affinity of YtfQ for galactofuranose is 0.13μM; YtfQ is able to recognise both α and β forms of galactofuranose; YtfQ does not bind glucose . The crystal structure of YtfQ with a single molecule of galactofuranose in its ligand binding pocket has been resolved at 1.2Å. The binding protein has two α/β domains linked by a hinge region; galactofuranose binds in a cleft between the two domains and is totally buried within the protein; a disulfide bond is present between cysteine residues 129 and 193 . YtfQ is upregulated in fed-batch phase (compared to exponential phase) during glucose-limited fermentation .

## Biological Role

Component of galactofuranose ABC transporter (complex.ecocyc.ABC-46-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex YtfQRT-YjfF involved in galactofuranose transport (Probable). Binds to both alpha- and beta-galactofuranose (PubMed:19744923). {ECO:0000269|PubMed:19744923, ECO:0000305|PubMed:19744923}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-46-CPLX|complex.ecocyc.ABC-46-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4227|gene.b4227]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39325`
- `KEGG:ecj:JW4186;eco:b4227;ecoc:C3026_22825;`
- `GeneID:948746;`
- `GO:GO:0005534; GO:0015757; GO:0030288; GO:0048029; GO:0055052; GO:0140271`

## Notes

Galactofuranose-binding protein YtfQ
