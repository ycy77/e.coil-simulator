---
entity_id: "protein.P69913"
entity_type: "protein"
name: "csrA"
source_database: "UniProt"
source_id: "P69913"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00167}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "csrA zfiA b2696 JW2666"
---

# csrA

`protein.P69913`

## Static

- Type: `protein`
- Source: `UniProt:P69913`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00167}.

## Enriched Summary

FUNCTION: A key translational regulator that binds mRNA to regulate translation initiation and/or mRNA stability, initially identified for its effects on central carbon metabolism (PubMed:8393005). Mediates global changes in gene expression, shifting from rapid growth to stress survival by linking envelope stress, the stringent response and the catabolite repression systems (PubMed:21488981, PubMed:28924029). Binds to the 5'-UTR of mRNA to repress or activate translation; 2 binding sites on the homodimer can bridge 2 sites within target RNA (By similarity). Exerts reciprocal effects on enzymes of gluconeogenesis and glycogen biosynthesis versus those of glycolysis (PubMed:16923806, PubMed:7493933). Negatively effects glycogen biosynthesis, gluconeogenesis, alters cell size and surface properties (PubMed:7493933, PubMed:7751274, PubMed:8393005). Activates regulates expression of glycolysis genes (PubMed:7493933). Represses biofilm formation (PubMed:11741870). Regulates glycogen synthesis under both aerobic and anaerobic conditions; overexpression strongly inhibits glycogen accumulation (PubMed:8393005). Binds to 4 sites in its own promoter, including the Shine-Dalgarno sequence, repressing its own translation; mutating the binding-sites decreases repression (PubMed:21696456)...

## Biological Role

Component of CsrA complex with CsrB RNA (complex.ecocyc.CPLX0-1041), carbon storage regulator CsrA (complex.ecocyc.CPLX0-7956), CsrA complex with CsrC RNA (complex.ecocyc.CPLX0-8253).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

FUNCTION: A key translational regulator that binds mRNA to regulate translation initiation and/or mRNA stability, initially identified for its effects on central carbon metabolism (PubMed:8393005). Mediates global changes in gene expression, shifting from rapid growth to stress survival by linking envelope stress, the stringent response and the catabolite repression systems (PubMed:21488981, PubMed:28924029). Binds to the 5'-UTR of mRNA to repress or activate translation; 2 binding sites on the homodimer can bridge 2 sites within target RNA (By similarity). Exerts reciprocal effects on enzymes of gluconeogenesis and glycogen biosynthesis versus those of glycolysis (PubMed:16923806, PubMed:7493933). Negatively effects glycogen biosynthesis, gluconeogenesis, alters cell size and surface properties (PubMed:7493933, PubMed:7751274, PubMed:8393005). Activates regulates expression of glycolysis genes (PubMed:7493933). Represses biofilm formation (PubMed:11741870). Regulates glycogen synthesis under both aerobic and anaerobic conditions; overexpression strongly inhibits glycogen accumulation (PubMed:8393005). Binds to 4 sites in its own promoter, including the Shine-Dalgarno sequence, repressing its own translation; mutating the binding-sites decreases repression (PubMed:21696456). Indirectly activates transcription from 1 of its 5 promoters, which is responsible for increased expression during stationary phase (PubMed:21696456). Binds to at least 720 transcripts in strain K12 / CF7789, many of which are also part of the stringent response, including relA, spoT and dksA; slightly represses RelA and slightly activates DskA translation (PubMed:21488981). Binds to and represses the ECF sigma factor rpoE promoter (PubMed:28924029). Accelerates the degradation of glgC gene transcripts; overexpression further decreases glgC transcripts (PubMed:7751274). Binds 2 sites in the glgC mRNA leader, 1 of which overlaps the Shine-Dalgarno sequence, preventing ribosome-binding and thus destabilizing the mRNA (PubMed:12067347). Acts to inhibit interaction between the CcdB (also known as LetD) protein and the A subunit of DNA gyrase (PubMed:8604133). Required to activate motility and flagellum biosynthesis through the post-transcriptional activation of flhDC expression by binding to and stabilizing the flhDC message (PubMed:11298291). Represses translation of iraD mRNA via translational coupling to an upstream open reading frame (PubMed:28851853). Binds to mRNA and reduces levels of probable diguanylate cyclases dgcT and dgcZ (PubMed:18713317). {ECO:0000250|UniProtKB:P0DPC3, ECO:0000269|PubMed:11298291, ECO:0000269|PubMed:11741870, ECO:0000269|PubMed:12067347, ECO:0000269|PubMed:16923806, ECO:0000269|PubMed:18713317, ECO:0000269|PubMed:19460094, ECO:0000269|PubMed:21488981, ECO:0000269|PubMed:21696456, ECO:0000269|PubMed:28851853, ECO:0000269|PubMed:28924029, ECO:0000269|PubMed:7493933, ECO:0000269|PubMed:7751274, ECO:0000269|PubMed:8393005, ECO:0000269|PubMed:8604133}.; FUNCTION: Binds to and is sequestered by non-coding small RNAs (sRNA) CsrB and CsrC which antagonize the activity of CsrA (PubMed:12694612, PubMed:9211896). The consensus RNA-binding site is CAGGA(U/A/C)G which is located in probable hairpin loops (PubMed:9211896). There are 18 sites in CsrB, which cooperatively binds about 18 copies of CsrA (PubMed:12694612, PubMed:9211896). CsrC has 9 sites, and cooperatively binds multiple copies of CsrA (PubMed:12694612). Indirectly activates expression of CsrB and CsrC, both dependently and independently of the BarA-UvrY two-component system (PubMed:12193630, PubMed:12694612). ppGpp activates transcription of CsrA-antagonistic small RNAs CsrB and CsrC, which down-regulates CsrA's action on translation during the stringent response (PubMed:21488981). {ECO:0000269|PubMed:12193630, ECO:0000269|PubMed:12694612, ECO:0000269|PubMed:9211896}.

## Pathways

- `eco02020` Two-component system (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (31)

- `activates` --> [[gene.b0781|gene.b0781]] `RegulonDB` `C` - regulator=CsrA; target=moaA; function=+
- `activates` --> [[gene.b0782|gene.b0782]] `RegulonDB` `C` - regulator=CsrA; target=moaB; function=+
- `activates` --> [[gene.b0783|gene.b0783]] `RegulonDB` `C` - regulator=CsrA; target=moaC; function=+
- `activates` --> [[gene.b0784|gene.b0784]] `RegulonDB` `C` - regulator=CsrA; target=moaD; function=+
- `activates` --> [[gene.b0785|gene.b0785]] `RegulonDB` `C` - regulator=CsrA; target=moaE; function=+
- `activates` --> [[gene.b1044|gene.b1044]] `RegulonDB|EcoCyc` `S` - regulator=CsrA; target=ymdA; function=+ | EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation
- `is_component_of` --> [[complex.ecocyc.CPLX0-1041|complex.ecocyc.CPLX0-1041]] `EcoCyc` `database` - EcoCyc component coefficient=18
- `is_component_of` --> [[complex.ecocyc.CPLX0-7956|complex.ecocyc.CPLX0-7956]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-8253|complex.ecocyc.CPLX0-8253]] `EcoCyc` `database` - EcoCyc component coefficient=9
- `represses` --> [[gene.b0020|gene.b0020]] `RegulonDB` `S` - regulator=carbon storage regulator CsrA; target=nhaR; function=-
- `represses` --> [[gene.b1021|gene.b1021]] `RegulonDB` `C` - regulator=carbon storage regulator CsrA; target=pgaD; function=-
- `represses` --> [[gene.b1022|gene.b1022]] `RegulonDB` `C` - regulator=carbon storage regulator CsrA; target=pgaC; function=-
- `represses` --> [[gene.b1023|gene.b1023]] `RegulonDB` `C` - regulator=carbon storage regulator CsrA; target=pgaB; function=-
- `represses` --> [[gene.b1024|gene.b1024]] `RegulonDB` `C` - regulator=carbon storage regulator CsrA; target=pgaA; function=-
- `represses` --> [[gene.b1276|gene.b1276]] `RegulonDB` `C` - regulator=carbon storage regulator CsrA; target=acnA; function=-
- `represses` --> [[gene.b1492|gene.b1492]] `RegulonDB` `S` - regulator=CsrA; target=gadC; function=-
- `represses` --> [[gene.b1493|gene.b1493]] `RegulonDB|EcoCyc` `S` - regulator=CsrA; target=gadB; function=- | EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation
- `represses` --> [[gene.b1499|gene.b1499]] `EcoCyc` `database` - EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation
- `represses` --> [[gene.b1535|gene.b1535]] `RegulonDB` `S` - regulator=carbon storage regulator CsrA; target=dgcZ; function=-
- `represses` --> [[gene.b1916|gene.b1916]] `RegulonDB` `C` - regulator=carbon storage regulator CsrA; target=sdiA; function=-
- `represses` --> [[gene.b2369|gene.b2369]] `RegulonDB` `C` - regulator=carbon storage regulator CsrA; target=evgA; function=-
- `represses` --> [[gene.b2573|gene.b2573]] `RegulonDB|EcoCyc` `C` - regulator=CsrA; target=rpoE; function=- | EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation
- `represses` --> [[gene.b3428|gene.b3428]] `RegulonDB` `S` - regulator=carbon storage regulator CsrA; target=glgP; function=-
- `represses` --> [[gene.b3429|gene.b3429]] `RegulonDB` `S` - regulator=carbon storage regulator CsrA; target=glgA; function=-
- `represses` --> [[gene.b3430|gene.b3430]] `RegulonDB` `S` - regulator=carbon storage regulator CsrA; target=glgC; function=-
- `represses` --> [[gene.b3512|gene.b3512]] `EcoCyc` `database` - EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation
- `represses` --> [[gene.b3517|gene.b3517]] `RegulonDB|EcoCyc` `S` - regulator=CsrA; target=gadA; function=- | EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation
- `represses` --> [[gene.b4326|gene.b4326]] `RegulonDB` `S` - regulator=CsrA; target=iraD; function=-
- `represses` --> [[gene.b4720|gene.b4720]] `RegulonDB` `S` - regulator=CsrA; target=ytiC; function=-
- `represses` --> [[gene.b4721|gene.b4721]] `RegulonDB` `S` - regulator=CsrA; target=ytiD; function=-
- `represses` --> [[gene.b4722|gene.b4722]] `RegulonDB` `S` - regulator=CsrA; target=idlP; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b2696|gene.b2696]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69913`
- `KEGG:ecj:JW2666;eco:b2696;ecoc:C3026_14840;`
- `GeneID:947176;99707129;99809205;`
- `GO:GO:0005829; GO:0006109; GO:0006402; GO:0017148; GO:0045947; GO:0045948; GO:0048027; GO:0048255`

## Notes

Carbon storage regulator (Translational dual regulator CsrA)
