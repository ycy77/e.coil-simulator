---
entity_id: "protein.P0AGL7"
entity_type: "protein"
name: "rsmE"
source_database: "UniProt"
source_id: "P0AGL7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rsmE yggJ b2946 JW2913"
---

# rsmE

`protein.P0AGL7`

## Static

- Type: `protein`
- Source: `UniProt:P0AGL7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Specifically methylates the N3 position of the uracil ring of uridine 1498 (m3U1498) in 16S rRNA. Acts on the fully assembled 30S ribosomal subunit. {ECO:0000269|PubMed:16431987, ECO:0000269|PubMed:17872509}. RsmE is the methyltransferase responsible for methylation of 16S rRNA at the N3 position of the U1498 nucleotide . In vitro, RsmE can methylate 16S rRNA within the assembled 30S ribosomal subunit, but not 70S ribosomes or naked 16S rRNA . RsmE belongs to the DUF family of predicted α/β trefoil knot methyltransferases . Crystal and solution structures of RsmE showed an N-terminal RNA recognition and binding domain and a C-terminal conserved methyltransferase domain containing a deep trefoil knot. Site-directed mutagenesis of residues based on the RsmE structure confirmed the key residues required for methyltransferase activity. A catalytic mechanism has been proposed . A strain carrying a deletion of rsmE appears to have no growth defect when grown alone, but can not compete with isogenic wild-type cells when grown in mixed culture .

## Biological Role

Component of 16S rRNA m3U1498 methyltransferase (complex.ecocyc.CPLX0-7727).

## Annotation

FUNCTION: Specifically methylates the N3 position of the uracil ring of uridine 1498 (m3U1498) in 16S rRNA. Acts on the fully assembled 30S ribosomal subunit. {ECO:0000269|PubMed:16431987, ECO:0000269|PubMed:17872509}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7727|complex.ecocyc.CPLX0-7727]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2946|gene.b2946]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AGL7`
- `KEGG:ecj:JW2913;eco:b2946;ecoc:C3026_16125;`
- `GeneID:75173052;945816;`
- `GO:GO:0005737; GO:0042803; GO:0070042; GO:0070475`
- `EC:2.1.1.193`

## Notes

Ribosomal RNA small subunit methyltransferase E (EC 2.1.1.193) (16S rRNA m3U1498 methyltransferase)
