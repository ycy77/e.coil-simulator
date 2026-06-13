---
entity_id: "protein.P0A9F6"
entity_type: "protein"
name: "gcvA"
source_database: "UniProt"
source_id: "P0A9F6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gcvA b2808 JW2779"
---

# gcvA

`protein.P0A9F6`

## Static

- Type: `protein`
- Source: `UniProt:P0A9F6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Regulatory protein for the glycine cleavage system operon (gcv). Mediates activation of gcv by glycine and repression by purines. GcvA is negatively autoregulated. Binds to three sites upstream of the gcv promoter. "Glycine cleavage A," GcvA, is a repressor of the glycine cleavage enzyme system, which is a secondary pathway for production of C1 units . It is negatively autoregulated, and it coordinately activates transcription of a small-RNA divergent gene . In the absence of glycine and the presence of GcvR, GcvA represses operons involved in the glycine cleavage system . GcvR is an accessory protein that binds directly to GcvA, bending DNA to form a repression complex (GcvA/GcvR) in the regulatory region of the gcvT operon . Glycine binds directly to GcvR to disrupt or block the association of the GcvA/GcvR complex, whereas purines appear to promote the formation of the repression complex through an unknown mechanism . GcvA also activates transcription of the gcv genes, via interaction with the α or σ subunits of RNA polymerase . This transcriptional dual regulator, which belongs to the LysR-family , has two domains: the amino-terminal domain, which appears to be involved in transcription activation and in DNA binding through its helix-turn-helix subdomain, and the carboxy-terminal domain, involved in GcvR interaction...

## Biological Role

Component of GcvA-glycine (complex.ecocyc.CPLX0-8060).

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

FUNCTION: Regulatory protein for the glycine cleavage system operon (gcv). Mediates activation of gcv by glycine and repression by purines. GcvA is negatively autoregulated. Binds to three sites upstream of the gcv promoter.

## Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (9)

- `activates` --> [[gene.b2903|gene.b2903]] `RegulonDB` `C` - regulator=GcvA; target=gcvP; function=-+
- `activates` --> [[gene.b2904|gene.b2904]] `RegulonDB` `C` - regulator=GcvA; target=gcvH; function=-+
- `activates` --> [[gene.b2905|gene.b2905]] `RegulonDB` `C` - regulator=GcvA; target=gcvT; function=-+
- `activates` --> [[gene.b4443|gene.b4443]] `RegulonDB` `C` - regulator=GcvA; target=gcvB; function=+
- `is_component_of` --> [[complex.ecocyc.CPLX0-8060|complex.ecocyc.CPLX0-8060]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b2808|gene.b2808]] `RegulonDB` `C` - regulator=GcvA; target=gcvA; function=-
- `represses` --> [[gene.b2903|gene.b2903]] `RegulonDB` `C` - regulator=GcvA; target=gcvP; function=-+
- `represses` --> [[gene.b2904|gene.b2904]] `RegulonDB` `C` - regulator=GcvA; target=gcvH; function=-+
- `represses` --> [[gene.b2905|gene.b2905]] `RegulonDB` `C` - regulator=GcvA; target=gcvT; function=-+

## Incoming Edges (1)

- `encodes` <-- [[gene.b2808|gene.b2808]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9F6`
- `KEGG:ecj:JW2779;eco:b2808;ecoc:C3026_15435;`
- `GeneID:86860889;93779190;947278;`
- `GO:GO:0003700; GO:0005737; GO:0006351; GO:0006355; GO:0009411; GO:0043565`

## Notes

Glycine cleavage system transcriptional activator (Gcv operon activator)
