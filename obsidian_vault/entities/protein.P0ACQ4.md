---
entity_id: "protein.P0ACQ4"
entity_type: "protein"
name: "oxyR"
source_database: "UniProt"
source_id: "P0ACQ4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "oxyR momR mor b3961 JW3933"
---

# oxyR

`protein.P0ACQ4`

## Static

- Type: `protein`
- Source: `UniProt:P0ACQ4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Hydrogen peroxide (H2O2) sensor. Activates the expression of a regulon of H2O2-inducible genes such as katG, gor, ahpC, ahpF, oxyS (a regulatory RNA), dps, fur and grxA in response to H2O2. Represses transcription of phage Mu mom gene in a methylation-sensitive manner; MomR binds to the mom promoter when it is unmethylated but not if it is fully methylated (PubMed:2551682). Binds DNA in the upstream regions of its target genes; more than one site may be present per gene (PubMed:1864839, PubMed:2471187, PubMed:2551682). OxyR is inactivated by reduction of its essential disulfide bond by glutaredoxin (Grx1, grxA), itself positively regulated by OxyR (PubMed:9497290). Also has a positive regulatory effect on the production of surface proteins that control the colony morphology and auto-aggregation ability (PubMed:15659678). {ECO:0000269|PubMed:15659678, ECO:0000269|PubMed:1864839, ECO:0000269|PubMed:2551682, ECO:0000269|PubMed:9497290}. OxyR, "oxidative stress regulator," is the transcriptional dual regulator for the expression of antioxidant genes in response to oxidative stress, particularly, elevated levels of hydrogen peroxide. The OxyR regulon includes genes involved in peroxide metabolism, redox balance, and peroxide protection by, for example, manganese uptake . Moreover, OxyR activates the synthesis of the small, noncoding oxyS RNA...

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

FUNCTION: Hydrogen peroxide (H2O2) sensor. Activates the expression of a regulon of H2O2-inducible genes such as katG, gor, ahpC, ahpF, oxyS (a regulatory RNA), dps, fur and grxA in response to H2O2. Represses transcription of phage Mu mom gene in a methylation-sensitive manner; MomR binds to the mom promoter when it is unmethylated but not if it is fully methylated (PubMed:2551682). Binds DNA in the upstream regions of its target genes; more than one site may be present per gene (PubMed:1864839, PubMed:2471187, PubMed:2551682). OxyR is inactivated by reduction of its essential disulfide bond by glutaredoxin (Grx1, grxA), itself positively regulated by OxyR (PubMed:9497290). Also has a positive regulatory effect on the production of surface proteins that control the colony morphology and auto-aggregation ability (PubMed:15659678). {ECO:0000269|PubMed:15659678, ECO:0000269|PubMed:1864839, ECO:0000269|PubMed:2551682, ECO:0000269|PubMed:9497290}.

## Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (41)

- `activates` --> [[gene.b0475|gene.b0475]] `RegulonDB` `S` - regulator=OxyR; target=hemH; function=+
- `activates` --> [[gene.b0604|gene.b0604]] `RegulonDB` `S` - regulator=OxyR; target=dsbG; function=+
- `activates` --> [[gene.b0605|gene.b0605]] `RegulonDB` `S` - regulator=OxyR; target=ahpC; function=+
- `activates` --> [[gene.b0606|gene.b0606]] `RegulonDB` `S` - regulator=OxyR; target=ahpF; function=+
- `activates` --> [[gene.b0683|gene.b0683]] `RegulonDB` `C` - regulator=OxyR; target=fur; function=+
- `activates` --> [[gene.b0812|gene.b0812]] `RegulonDB` `S` - regulator=OxyR; target=dps; function=+
- `activates` --> [[gene.b0849|gene.b0849]] `RegulonDB` `S` - regulator=OxyR; target=grxA; function=+
- `activates` --> [[gene.b0871|gene.b0871]] `RegulonDB` `S` - regulator=OxyR; target=poxB; function=+
- `activates` --> [[gene.b0872|gene.b0872]] `RegulonDB` `S` - regulator=OxyR; target=hcr; function=+
- `activates` --> [[gene.b0873|gene.b0873]] `RegulonDB` `S` - regulator=OxyR; target=hcp; function=+
- `activates` --> [[gene.b1679|gene.b1679]] `RegulonDB` `C` - regulator=OxyR; target=sufE; function=+
- `activates` --> [[gene.b1680|gene.b1680]] `RegulonDB` `C` - regulator=OxyR; target=sufS; function=+
- `activates` --> [[gene.b1681|gene.b1681]] `RegulonDB` `C` - regulator=OxyR; target=sufD; function=+
- `activates` --> [[gene.b1682|gene.b1682]] `RegulonDB` `C` - regulator=OxyR; target=sufC; function=+
- `activates` --> [[gene.b1683|gene.b1683]] `RegulonDB` `C` - regulator=OxyR; target=sufB; function=+
- `activates` --> [[gene.b1684|gene.b1684]] `RegulonDB` `C` - regulator=OxyR; target=sufA; function=+
- `activates` --> [[gene.b1749|gene.b1749]] `RegulonDB|EcoCyc` `S` - regulator=OxyR; target=xthA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1857|gene.b1857]] `RegulonDB` `S` - regulator=OxyR; target=znuA; function=+
- `activates` --> [[gene.b1858|gene.b1858]] `RegulonDB` `S` - regulator=OxyR; target=znuC; function=+
- `activates` --> [[gene.b1859|gene.b1859]] `RegulonDB` `S` - regulator=OxyR; target=znuB; function=+
- `activates` --> [[gene.b1973|gene.b1973]] `RegulonDB` `S` - regulator=OxyR; target=zinT; function=+
- `activates` --> [[gene.b2266|gene.b2266]] `RegulonDB` `C` - regulator=OxyR; target=elaB; function=-+
- `activates` --> [[gene.b2392|gene.b2392]] `RegulonDB` `C` - regulator=OxyR; target=mntH; function=+
- `activates` --> [[gene.b2582|gene.b2582]] `RegulonDB` `C` - regulator=OxyR; target=trxC; function=+
- `activates` --> [[gene.b3518|gene.b3518]] `RegulonDB` `C` - regulator=OxyR; target=ccp; function=+
- `activates` --> [[gene.b3828|gene.b3828]] `RegulonDB` `S` - regulator=OxyR; target=metR; function=+
- `activates` --> [[gene.b3829|gene.b3829]] `RegulonDB` `S` - regulator=OxyR; target=metE; function=+
- `activates` --> [[gene.b3942|gene.b3942]] `RegulonDB` `C` - regulator=OxyR; target=katG; function=+
- `activates` --> [[gene.b4458|gene.b4458]] `RegulonDB` `S` - regulator=OxyR; target=oxyS; function=+
- `activates` --> [[gene.b4567|gene.b4567]] `RegulonDB` `C` - regulator=OxyR; target=yjjZ; function=+
- `activates` --> [[gene.b4637|gene.b4637]] `RegulonDB` `C` - regulator=OxyR; target=uof; function=+
- `represses` --> [[gene.b0850|gene.b0850]] `RegulonDB` `S` - regulator=OxyR; target=ybjC; function=-
- `represses` --> [[gene.b0851|gene.b0851]] `RegulonDB` `C` - regulator=OxyR; target=nfsA; function=-
- `represses` --> [[gene.b0852|gene.b0852]] `RegulonDB` `C` - regulator=OxyR; target=rimK; function=-
- `represses` --> [[gene.b0853|gene.b0853]] `RegulonDB` `C` - regulator=OxyR; target=ybjN; function=-
- `represses` --> [[gene.b1203|gene.b1203]] `RegulonDB` `S` - regulator=OxyR; target=ychF; function=-
- `represses` --> [[gene.b2000|gene.b2000]] `RegulonDB` `C` - regulator=OxyR; target=flu; function=-
- `represses` --> [[gene.b2266|gene.b2266]] `RegulonDB` `C` - regulator=OxyR; target=elaB; function=-+
- `represses` --> [[gene.b3961|gene.b3961]] `RegulonDB` `S` - regulator=OxyR; target=oxyR; function=-
- `represses` --> [[gene.b4367|gene.b4367]] `RegulonDB` `C` - regulator=OxyR; target=fhuF; function=-
- `represses` --> [[gene.b4435|gene.b4435]] `RegulonDB` `C` - regulator=OxyR; target=isrC; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b3961|gene.b3961]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACQ4`
- `KEGG:ecj:JW3933;eco:b3961;ecoc:C3026_21405;`
- `GeneID:75169405;75203207;948462;`
- `GO:GO:0000987; GO:0003700; GO:0005829; GO:0006355; GO:0006974; GO:0006979; GO:0032993; GO:0051409; GO:2000142`

## Notes

DNA-binding transcriptional dual regulator OxyR (Hydrogen peroxide-inducible genes activator) (Morphology and auto-aggregation control protein)
